import matplotlib.pyplot as plt
import numpy as np

# Gruppen und ihre pass@1-Werte
cm_pass1 = [28.05, 47.56, 60.37, 75.0, 31.10]  # Code Models
gm_pass1 = [50.0, 29.27, 25.0, 79.27, 31.71]   # Generalist Models

# Mittelwerte berechnen
cm_mean = np.mean(cm_pass1)
gm_mean = np.mean(gm_pass1)

# Standardabweichung (optional für Fehlerbalken)
cm_std = np.std(cm_pass1)
gm_std = np.std(gm_pass1)

# Balkenpositionen
labels = ['Code Models (CM)', 'Generalist Models (GM)']
x_pos = np.arange(len(labels))
means = [cm_mean, gm_mean]
errors = [cm_std, gm_std]  # Optional: Fehlerbalken

# Plot
plt.figure(figsize=(8, 6))
bars = plt.bar(x_pos, means, yerr=errors, align='center', alpha=0.9, capsize=10, color=['orange', 'steelblue'])

# Prozentwerte über den Balken anzeigen
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}%", ha='center', va='bottom', fontsize=14)

# Achsen und Layout
plt.ylabel("pass@1 [%]", fontsize=14)
plt.title("Durchschnittliche Modellleistung pro Gruppe", fontsize=16)
plt.xticks(x_pos, labels, fontsize=13)
plt.yticks(fontsize=13)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Anzeigen
plt.show()
