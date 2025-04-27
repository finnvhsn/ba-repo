from scipy.stats import mannwhitneyu


cm_values = [46.95, 27.44, 59.76, 78.66, 30.49]  
gm_values = [28.66, 49.39, 24.39, 74.39, 31.10]  


stat, p_value = mannwhitneyu(cm_values, gm_values, alternative='two-sided')


print(f"Mann-Whitney-U-Statistik: {stat}")
print(f"p-Wert: {p_value:.4f}")


"""
OUTPUT:
Mann-Whitney-U-Statistik: 15.0
p-Wert: 0.6905

"""