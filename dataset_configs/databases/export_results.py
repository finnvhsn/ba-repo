import sqlite3
import pandas as pd
import os
import argparse

# Argumente parsen
parser = argparse.ArgumentParser(description="Exportiere Ergebnisse aus SQLite nach Excel.")
parser.add_argument("--dataset", type=str, required=True, help="Name der Datenbank (z. B. humaneval oder mbpp)")
parser.add_argument("--model", type=str, required=True, help="Name des Modells (z. B. wizardcoder)")
args = parser.parse_args()

# Absoluter Pfad zum aktuellen Verzeichnis (da liegt das Skript)
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, f"{args.dataset}.db")

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect(DB_PATH)

# Daten laden
df = pd.read_sql("SELECT * FROM results_evaluated", conn)

# Filtern nach Modell
df_model = df[df["model_name"] == args.model]

if df_model.empty:
    print(f"❌ Keine Ergebnisse für Modell '{args.model}' in Datensatz '{args.dataset}' gefunden.")
    exit(1)

# Exportverzeichnis
output_dir = os.path.join(BASE_DIR, "..", "exports_excel")
os.makedirs(output_dir, exist_ok=True)

# Exportieren
filename = f"{args.dataset}_{args.model}.xlsx"
output_path = os.path.join(output_dir, filename)
df_model.to_excel(output_path, index=False)
print(f"✅ Exportiert: {output_path}")
