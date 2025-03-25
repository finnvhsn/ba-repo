

def evaluate_model_output(prompt, model_output, test_code):
    try:
 
        full_code = prompt + "\n" + model_output + "\n" + test_code

    
        local_ns = {}

      
        exec(full_code, {}, local_ns)

      
        func_name = extract_function_name(prompt)
        candidate_func = local_ns.get(func_name)
        
        if candidate_func is None:
            return "error: candidate not found"

        local_ns["check"](candidate_func)

        return "passed"
    except AssertionError:
        return "failed"
    except Exception as e:
        return f"error: {type(e).__name__}"
    
    
def extract_function_name(prompt: str) -> str:
    for line in prompt.splitlines():
        line = line.strip()
        if line.startswith("def "):
            name_part = line.split("(")[0]  
            return name_part.replace("def ", "").strip()
    return None  

    
import sqlite3
import pandas as pd


conn = sqlite3.connect("humaneval.db")
df = pd.read_sql("SELECT * FROM results", conn)


results = []

for _, row in df.iterrows():
    result = evaluate_model_output(
        row["prompt"],
        row["model_output"],
        row["test_code"]
    )
    results.append(result)

df["test_result"] = results
df.to_sql("results_evaluated", conn, if_exists="replace", index=False)
