import numpy as np

# pass@1-Werte
cm_values = [47.56, 28.05, 60.37, 79.27, 31.10]  # Coding-Modelle
gm_values = [29.27, 50.0, 25.0, 75.0, 31.71]     # Generalistische Modelle

std_cm = np.std(cm_values, ddof=1) 
std_gm = np.std(gm_values, ddof=1)

print(f"Standardabweichung der Coding-Modelle: {std_cm:.2f}")
print(f"Standardabweichung der Generalistischen Modelle: {std_gm:.2f}")

"""
OUTPUT:
Standardabweichung CM: 21.25
Standardabweichung GM: 20.67
    
"""