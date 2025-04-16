import matplotlib.pyplot as plt

# Modellnamen und pass@1-Werte paarweise nach Hersteller gruppiert
labels = [
    "CodeGemma", "Gemma",                # Google
    "CodeLLaMA", "LLaMA 3",              # Meta
    "DeepSeek-Coder", "DeepSeek-LLM",    # DeepSeek
    "QwenCoder 2.5", "Qwen 2.5",         # Alibaba
    "WizardCoder", "Mistral"             # ohne Pendant
]
values = [46.95, 28.66, 27.44, 49.39, 59.76, 24.39, 78.66, 74.39, 30.49, 31.10]


# Farben zuordnen (blau für CM, grau für GM)
colors = [
    'lightblue', 'lightgrey',  # Google
    'lightblue', 'lightgrey',  # Meta
    'lightblue', 'lightgrey',  # DeepSeek
    'lightblue', 'lightgrey',  # Alibaba
    'lightblue', 'lightgrey'   # Sonstige
]

# Diagramm erstellen
plt.figure(figsize=(12, 6))
bars = plt.bar(labels, values, color=colors)

# Prozentwerte über Balken schreiben
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.2f}%", ha='center', va='bottom', fontsize=14)

# Legende
custom_lines = [
    plt.Line2D([0], [0], color='lightblue', lw=6),
    plt.Line2D([0], [0], color='lightgrey', lw=6)
]
plt.legend(custom_lines, ['Coding-Modelle (CM)', 'Generalistische Modelle (GM)'], loc='upper right')

# Achsentitel und Formatierung
plt.ylabel("Pass@1 in %", fontsize=18)
plt.ylim(0, 100)
plt.xticks(rotation=45, fontsize=18)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
