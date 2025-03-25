import requests
import pandas as pd
import sqlite3
from datasets import load_dataset

API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoderbase-1b?wait_for_model=true"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

dataset = load_dataset("openai_humaneval")

rows = []

for i in range(10):
    sample = dataset["test"][i]
    prompt = sample["prompt"]
    response = query({"inputs": prompt})
    
    try:
        model_output = response[0]["generated_text"]
    except:
        model_output = str(response)  

    row = {
        "task_id": sample["task_id"],
        "prompt": prompt,
        "canonical_solution": sample["canonical_solution"],
        "test_code": sample["test"],
        "model_output": model_output,
        "model_name": "starcoderbase-1b"
    }
    
    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("humaneval_output.csv", index=False )

conn = sqlite3.connect("humaneval.db")
df.to_sql("results", conn, if_exists="append", index=False)