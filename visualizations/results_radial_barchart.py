import matplotlib.pyplot as plt
import numpy as np

# Modellnamen und pass@1-Werte
labels = [
    "CodeGemma", "CodeLLaMA", "DeepSeek-Coder", "DeepSeek-LLM", "Gemma",
    "LLaMA 3", "Mistral", "QwenCoder 2.5", "Qwen 2.5", "WizardCoder"
]

values = [47.56, 28.05, 60.37, 25.0, 29.27, 50.0, 31.71, 79.27, 75.0, 31.10]
N = len(values)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Plot-Vorbereitung
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Balken zeichnen
bars = ax.bar(angles, values, width=2 * np.pi / N * 0.8, color='lightblue', alpha=0.9)

# Prozentzahlen in den Balken (schwarz)
for angle, value in zip(angles, values):
    ax.text(
        angle,
        value / 2,
        f"{int(round(value))}%",
        ha='center',
        va='center',
        fontsize=11,
        color='black',
        rotation=0
    )

# Modellnamen weiter außen platzieren
label_radius = 125  # weiter draußen
for angle, label in zip(angles, labels):
    ax.text(
        angle,
        label_radius,
        label,
        ha='center',
        va='center',
        rotation=0,
        fontsize=16
    )

# Hilfskreise (nur bei 50 % und 100 % beschriften)
ax.set_ylim(0, 120)
ax.set_yticks([25, 50, 75, 100])
ax.set_yticklabels(['', '50%', '', '100%'], fontsize=10)
ax.yaxis.grid(True, linestyle='--', linewidth=2.0, alpha=0.7)



ax.spines['polar'].set_visible(False)




# Keine radiale Achsenbeschriftung
ax.xaxis.set_visible(False)



# Kein Titel
plt.tight_layout()
plt.show()
