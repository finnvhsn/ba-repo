import matplotlib.pyplot as plt

# Benchmark-Namen und zugehörige Werte
models = [
   "AlphaCode", "ChatGPT", "Claude 3.5 Sonnet", "Claude3", "CodeGeeX", "CodeGen", 
   "CodeLLama", "CodeT5", "Codex", "DeepSeek-Coder", "DeepSeek-R1", "GPT-3.5, -3.5-Turbo",
   "GPT-4, -4o, -4o-mini", "GPT-J", "GPT-Neo", "Incoder", "LLaMA", "LLaMA 3",
   "Mistral", "PaLM", "PaLM-Coder", "PolyCoder", "StarCoder, -2", "WizardCoder"
]
anzahlen = [7, 8, 3, 4, 7, 15, 17, 3, 13, 10, 3, 13, 16, 5, 8, 7, 5, 7, 6, 3, 5, 6, 11, 7]

# Nach Größe sortieren (absteigend)
sorted_data = sorted(zip(anzahlen, models), reverse=True)
sorted_anzahlen, sorted_models = zip(*sorted_data)

# Diagramm erstellen
plt.figure(figsize=(14, 6))
bars = plt.bar(sorted_models, sorted_anzahlen, color="orange")

# Werte unter die Balken schreiben
for bar, wert in zip(bars, sorted_anzahlen):
    plt.text(bar.get_x() + bar.get_width()/2, -0.5,  # leicht unter dem Balken
             str(wert), ha='center', va='top', fontsize=14)

# Achsenbeschriftungen und Layout
plt.xticks(rotation=45, ha="right", fontsize=18)
plt.yticks(ticks=range(0, 21, 5), fontsize=18)  # Y-Achse in 5er-Schritten von 0 bis 20
plt.ylim(bottom=-5, top=20)  # Platz für Werte unter den Balken und Obergrenze setzen
plt.tight_layout()
plt.grid(axis='y')

# Diagramm anzeigen
plt.show()
