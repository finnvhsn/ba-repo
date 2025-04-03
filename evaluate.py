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

# 🔹 Model Output bereinigen
def clean_model_output(code: str) -> str:
    code = code.strip()

    # Entferne führende und abschließende Markdown- oder Docstring-Blöcke
    code = re.sub(r'^("""|\'\'\'|```)\n?', '', code)
    code = re.sub(r'\n?("""|\'\'\'|```)$', '', code)
    code = re.sub(r'("""|\'\'\'|```)', '', code)

    return code.strip()

# 🔹 Funktion umbenennen in "candidate"
def rename_to_candidate(code: str) -> str:
    return re.sub(r"def\s+\w+\s*\(", "def candidate(", code, count=1)

import ast

def remove_function_docstrings(code: str) -> str:
    class FunctionDocstringRemover(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            self.generic_visit(node)
            if (node.body and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Str)):
                node.body.pop(0)
            return node

        def visit_AsyncFunctionDef(self, node):
            return self.visit_FunctionDef(node)

    try:
        tree = ast.parse(code)
        tree = FunctionDocstringRemover().visit(tree)
        ast.fix_missing_locations(tree)
        return ast.unparse(tree)
    except Exception as e:
        print(f"⚠️ AST-Parsing failed: {e}")
        return code  # Fallback


# 🔹 Sicherer Code-Ausführung mit Timeout
def safe_exec(full_code, timeout=3.0):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=run_code, args=(q, full_code))
    p.start()
    p.join(float(timeout))
    if p.is_alive():
        p.terminate()
        return "error: timeout"
    return q.get() if not q.empty() else "error: unknown"

# 🔹 Gesamte Auswertung pro Modell-Ausgabe
def evaluate_model_output(model_output, test_code, timeout=3.0):
    prelude = "from typing import List, Dict, Tuple, Optional, Any\n"
    model_output = clean_model_output(model_output)
    model_output = remove_function_docstrings(model_output)
    model_output = rename_to_candidate(model_output)
    
    #print("🔍 Cleaned model output:\n", model_output)
    
    full_code = prelude + "\n" + model_output + "\n" + test_code
    return safe_exec(full_code, timeout=timeout)

# 🔹 Hauptausführung
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate LLM outputs for a given dataset.")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset name (e.g. humaneval or mbpp)")
    parser.add_argument("--model", type=str, required=True, help="Model name (e.g. codellama or wizardcoder)")
    parser.add_argument("--timeout", type=float, default=3.0, help="Timeout in seconds for each test")

    args = parser.parse_args()
    db_path = os.path.join("dataset_configs", "databases", f"{args.dataset}.db")
    table_name = f"{args.model}_results"

    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f'SELECT * FROM "{table_name}"', conn)

    print(f"🔍 Evaluating {len(df)} samples from table '{table_name}' ...")

    results = []
    for _, row in df.iterrows():
        result = evaluate_model_output(row["model_output"], row["test_code"], timeout=args.timeout)
        results.append(result)

    df["test_result"] = results

    # Tabelle aktualisieren
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print(f"✅ Evaluation complete. Results updated in table: {table_name}")
