import numpy as np

# Gruppenwerte (pass@1 in Prozent)
cm_values = [46.95, 27.44, 59.76, 78.66, 30.49]  # Coding-Modelle
gm_values = [28.66, 49.39, 24.39, 74.39, 31.10]  # Generalistische Modelle

# Median berechnen
median_cm = np.median(cm_values)
median_gm = np.median(gm_values)

print(f"Median CM: {median_cm:.2f}%")
print(f"Median GM: {median_gm:.2f}%")

"""
OUTPUT:
Median CM: 46.95%
Median GM: 31.10%

"""