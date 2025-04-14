import matplotlib.pyplot as plt

modelle = [
    "CodeGemma", "CodeLLaMA", "DeepSeek-Coder", "DeepSeek-LLM", "Gemma", 
    "LLaMA 3", "Mistral", "QwenCoder 2.5", "Qwen 2.5", "WizardCoder"
]

pass1_werte = [47.56, 28.05, 60.37, 25.0, 29.27, 50.0, 31.71, 79.27, 75.0, 31.10] 


sorted_data = sorted(zip(pass1_werte, modelle), reverse=True)
sorted_pass1, sorted_modelle = zip(*sorted_data)


plt.figure(figsize=(14, 6))
bars = plt.bar(sorted_modelle, sorted_pass1, color="lightblue")


for bar, wert in zip(bars, sorted_pass1):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f"{wert}%", ha='center', va='bottom', fontsize=14)


plt.ylabel("pass@1 in %", fontsize=16)


plt.xticks(rotation=45, ha="right", fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, 100)  
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
