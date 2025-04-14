import matplotlib.pyplot as plt
import numpy as np

# Modellgruppen
gm_models = [
    "Tabnine", "Copilot", "Gemini", "GPT", "GPT-J", "GPT-Neo", "ChatGPT", "Claude", "Bard", "PaLM",
    "Mistral", "Mixtral", "Gemma", "LLaMA", "Phi3", "BERT", "RoBERTa", "LaMDA", "Pythia"
]

cm_models = [
    "Code-cushman", "Codex", "PanGu-Coder", "InCoder", "CodeT5", "CodeLLaMA", "Magicoder", "CodeGemma", 
    "CodeQwen", "Nxcode-orpo", "CodeGen", "Minitron", "DeepSeek-Coder", "DeepSeek-R1", "DeepSeek-LLM", 
    "Granite-Coder", "StarCoder", "PaLM-Coder", "CodeBERT", "CodeGeex", "AlphaCode", "SantaCoder", 
    "Code-Davinci", "CodeParrot", "PolyCoder", "WizardCoder", "CodeWhisperer", "Codeium"
]

# Gleichmäßige horizontale Verteilung
x_gm = np.linspace(0, 0.45, len(gm_models))
y_gm = np.random.normal(loc=0.5, scale=0.05, size=len(gm_models))

x_cm = np.linspace(0.55, 1, len(cm_models))
y_cm = np.random.normal(loc=0.5, scale=0.05, size=len(cm_models))

# Plot vorbereiten
plt.figure(figsize=(20, 8))
plt.axvline(x=0.5, color='gray', linestyle='--')  # Trennlinie

# Punkte plotten
plt.scatter(x_gm, y_gm, color='steelblue', label='Generalistische Modelle')
plt.scatter(x_cm, y_cm, color='darkorange', label='Coding Modelle')

# Modellnamen beschriften
for x, y, label in zip(x_gm, y_gm, gm_models):
    plt.text(x, y + 0.03, label, va='bottom', ha='center', fontsize=10, rotation=45)

for x, y, label in zip(x_cm, y_cm, cm_models):
    plt.text(x, y + 0.03, label, va='bottom', ha='center', fontsize=10, rotation=45)

# Layout und Stil
plt.title('Modelleinteilung (GM vs. CM)', fontsize=16)
plt.yticks([])
plt.xticks([0, 0.5, 1], ["GM", "Trennung", "CM"])
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.xlabel('Modelltyp', fontsize=12)
plt.legend(loc='upper center', fontsize=12)
plt.box(False)
plt.tight_layout()
plt.show()
