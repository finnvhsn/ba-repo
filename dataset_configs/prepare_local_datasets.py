import os
import json
import random

# Basisverzeichnisse
BASE_DIR = os.path.dirname(__file__)
RAW_DIR = os.path.join(BASE_DIR, "raw_data")
LOCAL_DIR = os.path.join(BASE_DIR, "local_data")
os.makedirs(LOCAL_DIR, exist_ok=True)

# HumanEval laden
with open(os.path.join(RAW_DIR, "humaneval.jsonl"), "r", encoding="utf-8") as f:
    humaneval = [json.loads(line) for line in f]

with open(os.path.join(LOCAL_DIR, "humaneval.json"), "w", encoding="utf-8") as f:
    json.dump(humaneval, f, indent=2, ensure_ascii=False)

# MBPP laden + künstliche task_id hinzufügen
with open(os.path.join(RAW_DIR, "mbpp.jsonl"), "r", encoding="utf-8") as f:
    mbpp_all = []
    for idx, line in enumerate(f):
        obj = json.loads(line)
        obj["task_id"] = idx  # künstliche ID
        mbpp_all.append(obj)

# Filter: nur Beispiele mit test_asserts und task_id zwischen 11–510
mbpp_filtered = [ex for ex in mbpp_all if 11 <= ex["task_id"] <= 510 and ex.get("test_list")]


print(f"Gefundene Beispiele im Bereich 11–510 mit Tests: {len(mbpp_filtered)}")

if len(mbpp_filtered) < 164:
    raise ValueError(f"❌ Nur {len(mbpp_filtered)} passende Aufgaben gefunden. 164 benötigt.")

mbpp_sample = random.sample(mbpp_filtered, 164)

with open(os.path.join(LOCAL_DIR, "mbpp.json"), "w", encoding="utf-8") as f:
    json.dump(mbpp_sample, f, indent=2, ensure_ascii=False)

print("✅ HumanEval & MBPP wurden lokal gespeichert.")

