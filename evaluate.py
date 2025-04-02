import os
import argparse
import sqlite3
import pandas as pd
import multiprocessing
import re

# 🔹 Hilfsfunktion zum sicheren Ausführen von Code
def run_code(q, full_code):
    try:
        local_ns = {}
        exec(full_code, {}, local_ns)
        candidate_func = local_ns.get("candidate")
        if candidate_func is None:
            q.put("error: candidate not found")
            return
        local_ns["check"](candidate_func)
        q.put("passed")
    except AssertionError:
        q.put("failed")
    except Exception as e:
        q.put(f"error: {type(e).__name__}")

def rename_to_candidate(code: str) -> str:
    return re.sub(r"def\s+\w+\s*\(", "def candidate(", code, count=1)

def safe_exec(full_code, timeout=3):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=run_code, args=(q, full_code))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        return "error: timeout"
    return q.get() if not q.empty() else "error: unknown"

def evaluate_model_output(model_output, test_code):
    prelude = "from typing import List, Dict, Tuple, Optional, Any\n"
    model_output = rename_to_candidate(model_output)
    full_code = prelude + "\n" + model_output + "\n" + test_code
    return safe_exec(full_code)

# 🔹 Hauptausführung
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate LLM outputs for a given dataset.")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset name (e.g. humaneval or mbpp)")
    parser.add_argument("--model", type=str, required=True, help="Model name (e.g. codellama or wizardcoder)")

    args = parser.parse_args()
    db_path = os.path.join("dataset_configs", "databases", f"{args.dataset}.db")
    table_name = f"{args.model}_results"

    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f'SELECT * FROM "{table_name}"', conn)


    print(f"🔍 Evaluating {len(df)} samples from table '{table_name}' ...")

    results = []
    for _, row in df.iterrows():
        result = evaluate_model_output(row["model_output"], row["test_code"])
        results.append(result)

    df["test_result"] = results

    # Tabelle aktualisieren
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print(f"✅ Evaluation complete. Results updated in table: {table_name}")
