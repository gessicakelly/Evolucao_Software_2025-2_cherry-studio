# ===============================================
# Geração de gráfico de pizza dos sentimentos (estilo aprimorado)
# ===============================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do arquivo de resultados
arquivo = "resultados/resultados_sentimentos-model-tabularisai.csv"
modelo_nome = "tabularisai"

# Ler arquivo CSV
df = pd.read_csv(arquivo)

# Contar quantos sentimentos de cada tipo existem
contagem = df["Sentiment_3class"].value_counts(dropna=False)

# Criar pasta de saída se não existir
os.makedirs("resultados", exist_ok=True)

# Cores personalizadas (azul, laranja, verde, vermelho)
cores = ["#4B9CD3", "#F4A261", "#2A9D8F", "#E76F51"]

# Criar gráfico de pizza
fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
wedges, texts, autotexts = ax.pie(
    contagem,
    labels=contagem.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=cores[:len(contagem)],
    textprops={"color": "white", "weight": "bold"},
)

# Melhorar contraste das legendas externas
for t in texts:
    t.set_color("black")
    t.set_fontweight("medium")
    t.set_fontsize(11)

# Título
ax.set_title(
    f"Modelo: {modelo_nome}",
    fontsize=13,
    pad=15,
)
ax.axis("equal")  # Mantém formato circular

# Salvar e mostrar gráfico
saida_imagem = os.path.join("resultados", f"grafico_pizza_{modelo_nome}.png")
fig.savefig(saida_imagem, bbox_inches="tight", facecolor="white", dpi=300)
print(f"Gráfico salvo com sucesso: {saida_imagem}")

plt.show()
