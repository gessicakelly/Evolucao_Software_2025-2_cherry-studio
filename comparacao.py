# ============================================
# COMPARAÇÃO DE ANÁLISES DE SENTIMENTOS (dos 3 MODELOS)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# --- 1️Leitura dos três arquivos CSV ---
clapAI = pd.read_csv('Modelo 01 - ClapAI/resultados/resultados_sentimentos-model-clapAI.csv')
tabularisai = pd.read_csv('Modelo 02 - Tabularisai/resultados/resultados_sentimentos-model-tabularisai_com_truncamento.csv')
terrencewee12 = pd.read_csv('Modelo 03 - Terrencewee12/resultados/resultados_sentimentos-model-terrencewee12_com_truncamento.csv')

# --- 2Renomear colunas para identificar os modelos ---
clapAI = clapAI.rename(columns={
    'Sentiment': 'Sentiment_ClapAI'
})

tabularisai = tabularisai.rename(columns={
    'Sentiment_3class': 'Sentiment_TabularisAI'
})

terrencewee12 = terrencewee12.rename(columns={
    'Sentiment': 'Sentiment_TerrenceWee12'
})

# --- Função para normalizar os rótulos de sentimento ---
def padronizar_sentimentos(df, coluna_sentimento):
    df[coluna_sentimento] = df[coluna_sentimento].astype(str).str.strip().str.capitalize()
    return df

# Aplicar para cada modelo
clapAI = padronizar_sentimentos(clapAI, 'Sentiment_ClapAI')
tabularisai = padronizar_sentimentos(tabularisai, 'Sentiment_TabularisAI')
terrencewee12 = padronizar_sentimentos(terrencewee12, 'Sentiment_TerrenceWee12')

# --- Fazer merge dos três resultados (mantendo apenas as colunas necessárias) ---
comparacao = (
    clapAI[['PR_Number', 'Author', 'Comment', 'Sentiment_ClapAI']]
    .merge(tabularisai[['PR_Number', 'Author', 'Comment', 'Sentiment_TabularisAI']],
           on=['PR_Number', 'Author', 'Comment'], how='inner')
    .merge(terrencewee12[['PR_Number', 'Author', 'Comment', 'Sentiment_TerrenceWee12']],
           on=['PR_Number', 'Author', 'Comment'], how='inner')
)

# --- Criar coluna de concordância entre modelos ---
comparacao['Concordam'] = comparacao.apply(
    lambda x: len(set([
        x['Sentiment_ClapAI'],
        x['Sentiment_TabularisAI'],
        x['Sentiment_TerrenceWee12']
    ])) == 1,
    axis=1
)

# --- Calcular resumo percentual por modelo ---
resumo = {
    'ClapAI': clapAI['Sentiment_ClapAI'].value_counts(normalize=True) * 100,
    'TabularisAI': tabularisai['Sentiment_TabularisAI'].value_counts(normalize=True) * 100,
    'TerrenceWee12': terrencewee12['Sentiment_TerrenceWee12'].value_counts(normalize=True) * 100
}

resumo_df = pd.DataFrame(resumo).fillna(0).round(2)
print("\n==== Resumo Percentual de Sentimentos (Normalizado) ====\n")
print(resumo_df)

# --- Percentual de concordância ---
concordancia = comparacao['Concordam'].value_counts(normalize=True) * 100
print("\n==== Concordância entre os modelos ====\n")
print(concordancia)

# --- Visualização gráfica ---
melted = comparacao.melt(
    id_vars=['PR_Number', 'Comment'],
    value_vars=['Sentiment_ClapAI', 'Sentiment_TabularisAI', 'Sentiment_TerrenceWee12'],
    var_name='Modelo',
    value_name='Sentimento'
)

melted['Modelo'] = melted['Modelo'].str.replace('Sentiment_', '')

plt.figure(figsize=(8,5))
melted.groupby(['Modelo', 'Sentimento']).size().unstack().plot(kind='bar')
plt.title('Distribuição de Sentimentos por Modelo')
plt.ylabel('Número de Comentários')
plt.xlabel('Modelo')
plt.legend(title='Sentimento')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('./Saidas/grafico_comparativo_modelos.png', dpi=300, bbox_inches='tight')
plt.show()

# --- Exportar tabela comparativa final ---
comparacao.to_csv('./Saidas/comparacao_modelos.csv', index=False)
print("\n Arquivo 'comparacao_modelos.csv' gerado com sucesso!")
