# Evolucao_Software_2025-2_cherry-studio
Repositório da primeira atividade da disciplina de Evolução de Software, desenvolvido pela Equipe 02.

Integrantes:
- Géssica Kelly De Souza Santos
- Iago Humberto Da Rosa Normandia 
- Leticia Da Mata Cavalcanti 
- Maria Fernanda Da Mota Diniz 
- Pedro Henrique Gomes Dos Santos 
- Sammya Emanuelle Guimaraes De Oliveira 
- Wenderson Luiz Portela Da Silva
- Bruno Amancio Ferreira 

## 1. Estrutura do Projeto

- Entradas/ – Contém o CSV e JSON gerados pela coleta dos Pull Requests.

- Modelo X/ – Pasta do respectivo modelo.

   - nome_modelo.py – Script que executa o modelo.
   - gera_grafico.py – Gera gráficos dos resultados.
   - resultados/ – Guarda o CSV gerado e o gráfico do modelo.

- Saidas/ – Armazena o CSV de comparação entre os modelos e os gráficos finais.
- comparacao.py – Compara os resultados dos três modelos.
- script_dump.py – Coleta os Pull Requests e gera os arquivos de entrada.
- requirements.txt – Dependências do projeto.

## 2. Objetivo

Este projeto realiza uma análise de sentimentos sobre os comentários dos pull requests (PRs) do repositório cherry-studio, utilizando diferentes modelos de linguagem disponibilizados na plataforma Hugging Face.
O objetivo principal é compreender a percepção e o tom emocional dos desenvolvedores ao longo da evolução do projeto, identificando possíveis padrões de positividade, neutralidade e negatividade nas interações registradas nos PRs.


## 3. Etapas Realizadas

 a.  Coleta de Dados
   - Foram extraídos os 300 últimos pull requests fechados do projeto [`script_dump.py`]([link_para_o_arquivo_no_GitHub](https://github.com/gessicakelly/Evolucao_Software_2025-2_cherry-studio/blob/main/script_dump.py)) 
   - Cada PR teve seus comentários coletados (autor, número e comentario).
   - Os dados foram salvos em um arquivo JSON para posterior análise.

b. Modelos Utilizados
 - [ClapAI](https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment) 
 - [TabularisAI](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)
 - [TerrenceWee12](https://huggingface.co/terrencewee12/xlm-roberta-base-sentiment-multilingual-finetuned-v2)
 
Os modelos foram escolhidos por usarem categorias compatíveis com a atividade (positivo/negativo/ neutro) e por serem multilinguais, o que é essencial porque os comentários das PRs contêm mistura de idiomas.


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

## 4. Como executar 

a. Pré-requisitos:

Instale todas as dependências utilizando o arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

b. Rodar o script do modelo escolhido:

```
python tabularisai.py
python clapAI.py
python terencee.py
```

Ao final da execução, cada modelo gera um arquivo CSV com os resultados na sua respectiva pasta `resultados/`.

c. Rodar o script comparativo:

```
python comparacao.py
```
Esse script é responsável por analisar a correspondência entre os resultados e comparar o desempenho dos três modelos.




## 5. Conclusão

O projeto permitiu:

- Comparar o comportamento de diferentes modelos de análise de sentimentos.

- Identificar momentos de maior positividade ou negatividade nas interações do repositório.

- Observar o impacto emocional na evolução do projeto de software.

## 6. Infraestrutura utilizada
- Processador 11th Gen Intel(R) Core(TM) i5-11400F @ 2.60GHz (2.59 GHz)
- Memória RAM Kingston 16,0 GB DDR4 3200mHz
- Placa de vídeo: NVIDIA RTX 4060 T.I
- Sistema Operacional: Windows 11
