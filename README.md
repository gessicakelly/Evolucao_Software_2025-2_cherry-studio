# Evolucao_Software_2025-2_cherry-studio

Integrantes: 
- Bruno Amancio Ferreira
- Géssica Kelly De Souza Santos 
- Iago Humberto Da Rosa Normandia 
- Leticia Da Mata Cavalcanti 
- Maria Fernanda Da Mota Diniz 
- Pedro Henrique Gomes Dos Santos 
- Sammya Emanuelle Guimaraes De Oliveira 
- Wenderson Luiz Portela Da Silva 

## 1. Objetivo

Este projeto realiza uma análise de sentimentos sobre os comentários dos pull requests (PRs) do repositório cherry-studio, utilizando diferentes modelos de linguagem disponibilizados na plataforma Hugging Face.
O objetivo principal é compreender a percepção e o tom emocional dos desenvolvedores ao longo da evolução do projeto, identificando possíveis padrões de positividade, neutralidade e negatividade nas interações registradas nos PRs.


## 2. Etapas Realizadas

 a.  Coleta de Dados
   - Foram extraídos os 300 últimos pull requests fechados do projeto [`script_dump.py`]([link_para_o_arquivo_no_GitHub](https://github.com/gessicakelly/Evolucao_Software_2025-2_cherry-studio/blob/main/script_dump.py)) 
   - Cada PR teve seus comentários coletados (autor, número e comentario).
   - Os dados foram salvos em um arquivo JSON para posterior análise.

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

### Conclusão

O projeto permitiu:

- Comparar o comportamento de diferentes modelos de análise de sentimentos.

- Identificar momentos de maior positividade ou negatividade nas interações do repositório.

- Observar o impacto emocional na evolução do projeto de software.
