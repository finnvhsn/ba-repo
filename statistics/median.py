import numpy as np

# pass@1-Werte
cm_values = [47.56, 28.05, 60.37, 79.27, 31.10]  # Coding-Modelle
gm_values = [29.27, 50.0, 25.0, 75.0, 31.71]     # Generalistische Modelle

# Median berechnen
median_cm = np.median(cm_values)
median_gm = np.median(gm_values)

print(f"Median CM: {median_cm:.2f}%")
print(f"Median GM: {median_gm:.2f}%")

"""
OUTPUT:
Median CM: 47.56%
Median GM: 31.71%

"""