import os
import json
import argparse
import sqlite3
import pandas as pd
import time
import importlib
from common.query import query


def load_local_dataset(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_benchmark(dataset_config, model_name, num_samples=10):
    dataset_path = os.path.join("dataset_configs", "local_data", f"{dataset_config.DATASET_NAME}.json")
    dataset = load_local_dataset(dataset_path)
    results = []

    print(f"\n▶ Running model: {model_name}")
    start_time = time.time()

    for i in range(num_samples):
        sample = dataset[i]

        try:
            key_text = dataset_config.FIELDS["text"]
            if key_text not in sample:
                print(f"❌ Sample {i} missing expected key: '{key_text}'")
                print("🔍 Sample keys:", list(sample.keys()))
                continue

            task_text = sample[key_text]
            prompt = dataset_config.PROMPT_TEMPLATE.format(text=task_text)
        except Exception as e:
            print(f"❌ Error in sample {i}: {e}")
            print("🔍 Sample content:", sample)
            continue

        output = query(prompt, model=model_name)

        try:
            row = {
                "task_id": sample[dataset_config.FIELDS["task_id"]],
                "prompt": prompt,
                "canonical_solution": sample[dataset_config.FIELDS["solution"]],
                "test_code": ("\n".join(sample[dataset_config.FIELDS["test"]])
                              if isinstance(sample[dataset_config.FIELDS["test"]], list)
                              else sample[dataset_config.FIELDS["test"]]),
                "model_output": output,
                "model_name": model_name
            }
        except KeyError as e:
            print(f"❌ KeyError while building row in sample {i}: {e}")
            continue

        results.append(row)
        print(f"✅ Sample {i + 1}/{num_samples} completed")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(f"🕒 {model_name} took {total_time} seconds for {len(results)} completed samples")


    for row in results:
        row["time"] = total_time

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run LLM benchmark.")
    parser.add_argument("--dataset", type=str, required=True, help="Name of the dataset config (e.g. 'humaneval' or 'mbpp')")
    parser.add_argument("--models", nargs="+", required=True, help="List of model names to evaluate")
    parser.add_argument("--samples", type=int, default=10, help="Number of samples to process")

    args = parser.parse_args()

    try:
        config = importlib.import_module(f"dataset_configs.{args.dataset}_config")
    except ModuleNotFoundError:
        print(f"❌ Dataset config '{args.dataset}_config.py' not found in dataset_configs/")
        exit(1)


    csv_folder = os.path.join("dataset_configs", "exports")
    os.makedirs(csv_folder, exist_ok=True)
    db_folder = os.path.join("dataset_configs", "databases")
    os.makedirs(db_folder, exist_ok=True)
    db_path = os.path.join(db_folder, f"{args.dataset}.db")

    conn = sqlite3.connect(db_path)

    for model_name in args.models:
        results = run_benchmark(config, model_name, num_samples=args.samples)
        df = pd.DataFrame(results)

  
        for col in df.columns:
            df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, list) else x)

       
        csv_path = os.path.join(csv_folder, f"{args.dataset}_{model_name}.csv")
        df.to_csv(csv_path, index=False)
        print(f"✅ Saved {len(df)} results to 📄 {csv_path}")

      
        table_name = f"{model_name}_results"
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"🗃️  Saved to DB table: {table_name}")

    conn.close()
