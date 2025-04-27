import numpy as np


cm_values = [46.95, 27.44, 59.76, 78.66, 30.49]  
gm_values = [28.66, 49.39, 24.39, 74.39, 31.10] 

std_cm = np.std(cm_values, ddof=1) 
std_gm = np.std(gm_values, ddof=1)

print(f"Standardabweichung der Coding-Modelle: {std_cm:.2f}")
print(f"Standardabweichung der Generalistischen Modelle: {std_gm:.2f}")

"""
OUTPUT:
Standardabweichung der Coding-Modelle: 21.25
Standardabweichung der Generalistischen Modelle: 20.67
    
"""