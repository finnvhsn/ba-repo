import matplotlib.pyplot as plt

# Benchmark-Namen und zugehörige Werte
benchmarks = [
    "HumanEval", "HumanEval+", "MBPP", "MBPP+", "MHPP", "APPS", "GSM8K-Python", "EvoCodeBench", 
    "ClassEval", "MathQA-Python", "StudentEval", "CoderEval", "DS-1000", "PyBench", "SALLM", 
    "BigCodeBench", "DevEval", "ODEX", "BIG-Bench", "SWE Bench", "CodeBLEU", "Qiskit HumanEval", "ConCode"
]
anzahlen = [48, 6, 38, 2, 2, 20, 1, 1, 2, 2, 1, 5, 9, 1, 2, 5, 1, 2, 1, 2, 1, 1, 1]

# Nach Größe sortieren (absteigend)
sorted_data = sorted(zip(anzahlen, benchmarks), reverse=True)
sorted_anzahlen, sorted_benchmarks = zip(*sorted_data)

# Diagramm erstellen
plt.figure(figsize=(14, 6))
bars = plt.bar(sorted_benchmarks, sorted_anzahlen, color="lightblue")

# Werte unter die Balken schreiben
for bar, wert in zip(bars, sorted_anzahlen):
    plt.text(bar.get_x() + bar.get_width()/2, -0.5,  # leicht unter dem Balken
             str(wert), ha='center', va='top', fontsize=14)

# Achsentitel und Diagrammtitel
#plt.ylabel("Häufigkeit", fontsize=18)  # Größere Schrift für y-Achse


# Achsen anpassen und Layout optimieren
plt.xticks(rotation=45, ha="right", fontsize=18)  # Benchmark-Namen größer machen
plt.yticks(fontsize=18) 
plt.ylim(bottom=-5)  # Platz für Werte unter den Balken
plt.tight_layout()
plt.grid(axis='y')

# Diagramm anzeigen
plt.show()
