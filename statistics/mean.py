import numpy as np

# Gruppenwerte (pass@1 in Prozent)
cm_values = [46.95, 27.44, 59.76, 78.66, 30.49]  # Coding-Modelle
gm_values = [28.66, 49.39, 24.39, 74.39, 31.10]  # Generalistische Modelle

mean_cm = np.mean(cm_values)
mean_gm = np.mean(gm_values)

print(f"Mittelwert der Coding-Modelle: {mean_cm:.2f}%")
print(f"Mittelwert der Generalistischen Modelle: {mean_gm:.2f}%")

"""
OUTPUT:
Mittelwert der Coding-Modelle: 48.66%
Mittelwert der Generalistischen Modelle: 41.59%

"""