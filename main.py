import requests
import pandas as pd
import sqlite3
import json
from datasets import load_dataset
from prompt_template import PROMPT_TEMPLATE


def query(prompt, model="codellama", ip_adress="10.1.25.121"):
    chat_content = [{"role": "user", "content": prompt}]
    payload = {
        "model": model,
        "messages": chat_content,
        "stream": False
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'http://{ip_adress}:11434/api/chat', data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        return response.json()['message']['content']
    else:
        return f"[ERROR {response.status_code}] {response.text}"

dataset = load_dataset("openai_humaneval")

rows = []

for i in range(10):
    sample = dataset["test"][i]
    prompt = PROMPT_TEMPLATE.format(task_prompt=sample["prompt"])
    model_output = query(prompt) 

    row = {
        "task_id": sample["task_id"],
        "prompt": prompt,
        "canonical_solution": sample["canonical_solution"],
        "test_code": sample["test"],
        "model_output": model_output,
        "model_name": "codellama"
    }
    
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("humaneval_output.csv", index=False)

conn = sqlite3.connect("humaneval.db")
df.to_sql("results", conn, if_exists="replace", index=False)
