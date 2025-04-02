import sqlite3
import argparse
import os

def list_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    return tables

def delete_table(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    print(f"🗑️  Tabelle '{table_name}' gelöscht.")

def clear_table_contents(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    print(f"🧹 Inhalte aus Tabelle '{table_name}' gelöscht.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lösche Inhalte oder Tabellen aus einer SQLite-Datenbank.")
    parser.add_argument("--db", type=str, required=True, help="Name der Datenbankdatei (z. B. humaneval.db)")
    parser.add_argument("--table", type=str, help="Name der Tabelle, die gelöscht oder geleert werden soll")
    parser.add_argument("--drop", action="store_true", help="Tabelle komplett löschen statt nur leeren")

    args = parser.parse_args()

    db_path = os.path.join("dataset_configs", "databases", args.db)
    if not os.path.exists(db_path):
        print(f"❌ Datenbank nicht gefunden: {db_path}")
        exit(1)

    conn = sqlite3.connect(db_path)

    if args.table:
        if args.drop:
            delete_table(conn, args.table)
        else:
            clear_table_contents(conn, args.table)
    else:
        print("📋 Tabellen in der Datenbank:")
        for t in list_tables(conn):
            print(f" - {t}")

    conn.commit()
    conn.close()


