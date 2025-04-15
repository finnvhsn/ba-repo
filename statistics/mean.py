import numpy as np

# pass@1-Werte
cm_values = [47.56, 28.05, 60.37, 79.27, 31.10]  # Coding-Modelle
gm_values = [29.27, 50.0, 25.0, 75.0, 31.71]     # Generalistische Modelle

mean_cm = np.mean(cm_values)
mean_gm = np.mean(gm_values)

print(f"Mittelwert der Coding-Modelle: {mean_cm:.2f}%")
print(f"Mittelwert der Generalistischen Modelle: {mean_gm:.2f}%")

"""
OUTPUT:
Mittelwert CM: 49.27%
Mittelwert GM: 42.20%

"""