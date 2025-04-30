import matplotlib.pyplot as plt
import numpy as np

# Kategorien (Geschäftsbereiche)
categories = [
    "Strategy and Corporate Finance",
    "Supply Chain Management",
    "Marketing and Sales",
    "Service Operations",
    "Software Engineering",
    "Product or Service Development"
]

# Prozentuale Anteile pro Kategorie
gt_10 = np.array([11, 19, 8, 18, 12, 12])       # >10%
btw_6_10 = np.array([12, 15, 24, 14, 13, 15])   # 6–10%
lt_5 = np.array([47, 32, 34, 31, 31, 25])       # ≤5%

# Positionen für die y-Achse
y_pos = np.arange(len(categories))
totals = gt_10 + btw_6_10 + lt_5
max_total = max(totals)

# Diagramm erstellen
fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.barh(y_pos, gt_10, color='#a6a6a6', label='>10%')          
bar2 = ax.barh(y_pos, btw_6_10, left=gt_10, color='#7f7f7f', label='6–10%')  
bar3 = ax.barh(y_pos, lt_5, left=gt_10 + btw_6_10, color='#404040', label='≤5%')  

# Achsentitel und Diagrammtitel
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=12)
ax.set_xlabel("Anteil der Befragten", fontsize=12)
ax.set_title("Umsatzsteigerungen durch den Einsatz von KI\nnach Geschäftsbereich im 2. Halbjahr 2024")

# Prozentzahlen in die Balken schreiben
for bars in [bar1, bar2, bar3]:
    for bar in bars:
        width = bar.get_width()
        if width > 3:
            ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2,
                    f'{int(width)}%', ha='center', va='center',
                    fontsize=10, color='white')

# Gesamtwerte am Ende der Balken anzeigen
for i, total in enumerate(totals):
    ax.text(total + 1, y_pos[i], f'{total}%', va='center', ha='left', fontsize=10, color='black')

# Begrenzung der x-Achse leicht erweitern, um Text nicht abzuschneiden
ax.set_xlim(0, max_total + 10)

# Legende und Layout
ax.legend(loc='lower right')
plt.tight_layout()
plt.gca().invert_yaxis()
plt.show()
