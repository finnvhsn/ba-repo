from scipy.stats import mannwhitneyu

# Gruppenwerte (pass@1 in Prozent)
cm_values = [47.56, 28.05, 60.37, 79.27, 31.10]  # Coding-Modelle
gm_values = [29.27, 50.0, 25.0, 75.0, 31.71]     # Generalistische Modelle

# Mann-Whitney-U-Test durchführen (zweiseitig)
stat, p_value = mannwhitneyu(cm_values, gm_values, alternative='two-sided')

# Ergebnisse ausgeben
print(f"Mann-Whitney-U-Statistik: {stat}")
print(f"p-Wert: {p_value:.4f}")


"""
OUTPUT:
Mann-Whitney-U-Statistik: 15.0
p-Wert: 0.6905

"""