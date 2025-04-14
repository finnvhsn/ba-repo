import matplotlib.pyplot as plt
import numpy as np

# 10 Modellnamen
labels = [
    "CodeGemma", "CodeLLaMA", "DeepSeek-Coder", "DeepSeek-LLM", "Gemma", 
    "LLaMA 3", "Mistral", "QwenCoder 2.5", "Qwen 2.5", "WizardCoder"
]

# pass@1-Werte in exakt gleicher Reihenfolge
values = [47.56, 28.05, 60.37, 25.0, 29.27, 50.0, 31.71, 79.27, 75.0, 31.10]

# Kreis schließen: Ersten Wert wieder ans Ende anhängen
values += [values[0]]

# Winkel berechnen (eine Achse pro Label)
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += [angles[0]]  # Kreis schließen

# Plot vorbereiten
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Achsenbeschriftung (nur die 10 Labels)
ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=12)

# Skala
ax.set_ylim(0, 100)
ax.set_rlabel_position(0)
ax.yaxis.set_tick_params(labelsize=10)
ax.grid(True)

# Werte einzeichnen
ax.plot(angles, values, color='orange', linewidth=2)
ax.fill(angles, values, color='orange', alpha=0.25)

# Titel
plt.title("pass@1 auf HumanEval: Vergleich der Modelle", size=14, pad=20)
plt.tight_layout()
plt.show()
