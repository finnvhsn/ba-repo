import sqlite3

conn = sqlite3.connect("humaneval.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM results;")
cursor.execute("DELETE FROM results_evaluated;")

conn.commit()
conn.close()


