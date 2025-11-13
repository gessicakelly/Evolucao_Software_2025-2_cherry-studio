# Evolucao_Software_2025-2_cherry-studio

### 1. Coleta de Pull Requests
* Foram capturadas 300 Pull Requests.
* O script responsável pelo dump foi [`script_dump.py`]([link_para_o_arquivo_no_GitHub](https://github.com/gessicakelly/Evolucao_Software_2025-2_cherry-studio/blob/main/script_dump.py)) que gerou os arquivos em CSV e JSON presentes na pasta Entradas.

### 2. Modelos Utilizados

Cada modelo possui um script individual que realiza as seguintes etapas:

1. Recebe o modelo escolhido.
2. Carrega o modelo do Hugging Face.
3. Lê o arquivo JSON com os dados das PRs.
4. Faz a limpeza dos dados, descartando comentários vazios.
5. Executa a análise de sentimentos nos comentários válidos.
6. Salva os resultados em CSV para posterior análise.

| Modelo                                                               | URL                                                                                               | Observações                                                                            |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `clapAI/modernBERT-large-multilingual-sentiment`                     | [link](https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment)                     | Multilingual; não houve erros na leitura dos comentários; análise completa.            |
| `tabularisai/multilingual-sentiment-analysis`                        | [link](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)                        | Multilingual; houve alguns erros em textos muito grandes devido a limitação do modelo. |
| `terrencewee12/xlm-roberta-base-sentiment-multilingual-finetuned-v2` | [link](https://huggingface.co/terrencewee12/xlm-roberta-base-sentiment-multilingual-finetuned-v2) | Multilingual; erros ocasionais em textos muito grandes        |

---

### 3. Considerações Iniciais

1. **Primeiro modelo (`clapAI/modernBERT`)**

   * Mais completo.
   * Nenhum problema na leitura de comentários.
   * Capaz de identificar todo o texto, mesmo quando contém múltiplos idiomas.

2. **Segundo modelo (`tabularisai/multilingual-sentiment-analysis`)**

   * Também multitilingual.
   * Limitações apenas em textos muito longos, ocasionando erros.
   * Necessário ajuste para ignorar ou truncar textos grandes.

3. **Terceiro modelo (`terrencewee12/xlm-roberta-base`)**

   * Multilingual.
   * Mesma limitação de textos grandes, ajustada nos scripts.
   * Permitiu análise correta dos comentários válidos restantes.


### 4. Fluxo de Processamento dos Scripts

- JSON PRs → limpeza de comentários → seleção de comentários válidos → análise de sentimentos com modelo específico → exportação para CSV

<<<<<<< HEAD
* Cada script é adaptado para o modelo correspondente, mas o fluxo geral permanece o mesmo.
=======
b. Modelos Utilizados
 - [ClapAI](https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment) 
 - [TabularisAI](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)
 - [TerrenceWee12](https://huggingface.co/terrencewee12/xlm-roberta-base-sentiment-multilingual-finetuned-v2)
 
   Cada modelo foi executado separadamente, gerando um arquivo CSV com: 
   ```
   PR_Number | Author | Comment | Sentiment | Confidence
   ```
c. Tratamento dos Dados
- Implementado truncamento automático de textos longos (máx. 512 tokens) para evitar erros de execução.
- Padronização dos sentimentos em três classes principais:
   -  Positive
   - Neutral
   - Negative

d. Comparação Entre Modelos
- Os resultados foram mesclados em uma única [tabela comparativa](https://github.com/gessicakelly/Evolucao_Software_2025-2_cherry-studio/blob/main/Saidas/comparacao_modelos.csv).
- Calculado o percentual de cada sentimento por modelo.
- Avaliada a concordância entre os modelos (quantos PRs tiveram o mesmo sentimento nos três).
- Geração automática de gráficos e tabelas para visualização.

## Execução

a. Pré-requisitos:
```
pip install transformers pandas tqdm torch
```

b. Rodar o script do modelo escolhido:
```
python tabularisai.py
```
c. Rodar o script comparativo:
```
python comparacao.py
```

## Conclusão

O projeto permitiu:

- Comparar o comportamento de diferentes modelos de análise de sentimentos.

- Identificar momentos de maior positividade ou negatividade nas interações do repositório.

- Observar o impacto emocional na evolução do projeto de software.
>>>>>>> adb034844487b4e671e47d7b1ae54743fdd2fc37
