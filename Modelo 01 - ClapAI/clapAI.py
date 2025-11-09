# ===============================================
# Análise de Sentimentos - Modelo ClapAI
# https://huggingface.co/clapAI/modernBERT-large-multilingual-sentiment
# ===============================================
# Requisitos:
# pip install transformers
# pip install pandas 
# pip install tqdm
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# ===============================================

import os
os.environ["DISABLE_TRITON"] = "1"
os.environ["TORCH_COMPILE_DISABLE"] = "1"   # desativa TorchDynamo / AOTAutograd

import pandas as pd
from transformers import pipeline
from tqdm import tqdm
import torch

# Verificando se o CUDA esta´disponivel - o CUDA permite usar a GPU para acelerar os cálculos
print("CUDA disponível:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU detectada:", torch.cuda.get_device_name(0))
    print("Versão CUDA do PyTorch:", torch.version.cuda)


# Caminhos dos arquivos
entrada = "../entradas/cherry_prs.json"
saida = "resultados/resultados_sentimentos-model-clapAI.csv"

# Modelo escolhido
modelo = "clapAI/modernBERT-large-multilingual-sentiment"

# Detectar GPU automaticamente
device = 0 if torch.cuda.is_available() else -1  
print("Usando GPU para aceleração" if device == 0 else "Usando CPU (pode ser mais lento).")

# Carregar modelo
print(f"\nCarregando modelo: {modelo} ...")
analisador = pipeline("sentiment-analysis", model=modelo, device=device)
print("Modelo carregado com sucesso!\n")

# Ler arquivo JSON
df = pd.read_json(entrada)

# Limpeza: remover comentários vazios, nulos ou só com espaços(Irrelevantes para inspeção)
df = df[df["Comments"].notna()]
df["Comments"] = df["Comments"].astype(str).str.strip()
df = df[df["Comments"] != ""]

print(f"{len(df)} PRs com comentários válidos encontrados.\n")

# Lista para armazenar os resultados
resultados = []

# Analisar cada comentário válido
for _, linha in tqdm(df.iterrows(), total=len(df), desc="Analisando PRs"):
    texto = linha["Comments"]
    try:
        analise = analisador(texto)[0]
        resultados.append({
            "PR_Number": linha.get("PR_Number", None),
            "Author": linha.get("Author", None),
            "Comment": texto,
            "Sentiment": analise.get("label", "ERRO"),
            "Confidence": analise.get("score", 0.0)
        })
    except Exception as e:
        resultados.append({
            "PR_Number": linha.get("PR_Number", None),
            "Author": linha.get("Author", None),
            "Comment": texto,
            "Sentiment": "ERRO",
            "Confidence": 0.0
        })
        print(f"Erro ao processar comentário: {texto[:60]}... -> {str(e)}")

# Criar DataFrame final
df_resultados = pd.DataFrame(resultados)

# Salvar resultados em CSV
df_resultados.to_csv(saida, index=False, encoding="utf-8-sig")

print(f"\n Análise concluída com sucesso!")
print(f"Resultados salvos em: {saida}")