import matplotlib.pyplot as plt

# Modellnamen und pass@1-Werte
labels = [
    "QwenCoder 2.5", "DeepSeek-Coder", "CodeGemma", "WizardCoder", "CodeLLaMA",  # CM
    "Qwen 2.5", "LLaMA 3", "Mistral", "Gemma", "DeepSeek-LLM"                    # GM
]
values = [79.27, 60.37, 47.56, 31.10, 28.05, 75.0, 50.0, 31.71, 29.27, 25.0]

# Farbzuordnung pro Gruppe
colors = ['lightblue'] * 5 + ['lightgrey'] * 5

# Plot
plt.figure(figsize=(12, 6))
bars = plt.bar(labels, values, color=colors)

# Werte eintragen
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.2f}%", ha='center', va='bottom', fontsize=14)

# Trennlinie zwischen Gruppen
plt.axvline(x=4.5, color='gray', linestyle='--', linewidth=1)

# Legende hinzufügen
custom_lines = [
    plt.Line2D([0], [0], color='lightblue', lw=6),
    plt.Line2D([0], [0], color='lightgrey', lw=6)
]
plt.legend(custom_lines, ['Coding-Modelle (CM)', 'Generalistische Modelle (GM)'], loc='upper right')

# Achsentitel und Formatierung
plt.ylabel("Pass@1 in %", fontsize=18)
plt.ylim(0, 100)
plt.xticks(rotation=45, fontsize=18)  # Schriftgröße der Modellnamen auf 18 gesetzt
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
