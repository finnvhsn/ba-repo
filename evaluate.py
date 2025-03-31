import os
import json
import argparse
import sqlite3
import pandas as pd
import multiprocessing

# 🔹 Hilfsfunktion zum sicheren Ausführen von Code
def run_code(q, full_code, func_name):
    try:
        local_ns = {}
        exec(full_code, {}, local_ns)
        candidate_func = local_ns.get(func_name)
        if candidate_func is None:
            q.put("error: candidate not found")
            return
        local_ns["check"](candidate_func)
        q.put("passed")
    except AssertionError:
        q.put("failed")
    except Exception as e:
        q.put(f"error: {type(e).__name__}")

def safe_exec(full_code, func_name, timeout=3):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=run_code, args=(q, full_code, func_name))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        return "error: timeout"
    return q.get() if not q.empty() else "error: unknown"

def extract_function_name(prompt: str) -> str:
    for line in prompt.splitlines():
        line = line.strip()
        if line.startswith("def "):
            name_part = line.split("(")[0]
            return name_part.replace("def ", "").strip()
    return None

def evaluate_model_output(prompt, model_output, test_code):
    prelude = "from typing import List, Dict, Tuple, Optional, Any\n"
    full_code = prelude + "\n" + model_output + "\n" + test_code
    func_name = extract_function_name(prompt)
    return safe_exec(full_code, func_name)

# 🔹 Hauptausführung
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate LLM outputs against test cases.")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset name (e.g. humaneval or mbpp)")

    args = parser.parse_args()

    db_path = os.path.join("dataset_configs", "databases", f"{args.dataset}.db")
    conn = sqlite3.connect(db_path)

    # Ergebnisse lesen
    df = pd.read_sql("SELECT * FROM results", conn)

    # Bewertung durchführen
    print(f"🔍 Evaluating {len(df)} samples from '{args.dataset}' ...")
    results = []
    for _, row in df.iterrows():
        result = evaluate_model_output(
            row["prompt"],
            row["model_output"],
            row["test_code"]
        )
        results.append(result)

    df["test_result"] = results

    # Neue Tabelle abspeichern
    df.to_sql("results_evaluated", conn, if_exists="replace", index=False)
    print(f"✅ Evaluation complete. Results stored in 'results_evaluated' table at {db_path}")
