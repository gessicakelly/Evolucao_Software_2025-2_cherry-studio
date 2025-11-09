import requests
import csv
import json
import time
import re
from html import escape
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

repo = "CherryHQ/cherry-studio"
url = f"https://api.github.com/repos/{repo}/pulls"

GITHUB_TOKEN = ""  # Substitua pelo seu token pessoal

headers = {"Accept": "application/vnd.github.v3+json"}
if GITHUB_TOKEN:
    headers["Authorization"] = f"token {GITHUB_TOKEN}"

print(f"Coletando pull requests fechados do repositório {repo}...")

pulls = []
page = 1
max_prs = 300

while len(pulls) < max_prs:
    params = {
        "state": "closed",
        "per_page": 100,
        "page": page,
        "sort": "updated",
        "direction": "desc"
    }
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Erro {response.status_code}: {response.text}")
        break

    try:
        data_page = response.json()
    except ValueError:
        print(f"Erro ao converter resposta da página {page} em JSON.")
        break

    if not isinstance(data_page, list) or not data_page:
        print("Nenhum PR adicional encontrado.")
        break

    pulls.extend(data_page)
    print(f"Página {page} carregada ({len(data_page)} PRs). Total até agora: {len(pulls)}")
    page += 1
    time.sleep(0.4)

pulls = pulls[:max_prs]
print(f"Total de {len(pulls)} PRs fechados coletados.")

data = []

for i, pr in enumerate(pulls, start=1):
    comments_url = pr.get("comments_url")
    if not comments_url:
        continue

    try:
        comments_response = requests.get(comments_url, headers=headers, timeout=10)
        comments = comments_response.json()
    except Exception as e:
        print(f"Erro ao buscar comentários do PR #{pr.get('number')}: {e}")
        comments = []

    all_comments = " | ".join(
        [c["body"].replace("\n", " ") for c in comments if "body" in c and c["body"]]
    )

    data.append({
        "PR_Number": pr.get("number"),
        "PR_Title": pr.get("title", ""),
        "Author": pr.get("user", {}).get("login", "Desconhecido"),
        "Created_At": pr.get("created_at", ""),
        "Closed_At": pr.get("closed_at", ""),
        "Comments": all_comments,
        "State": pr.get("state", "")
    })

    print(f"Processado {i}/{len(pulls)} PRs")
    time.sleep(0.2)

if not data:
    print("Nenhum dado coletado.")
    exit()

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'\2 (\1)', text)
    text = re.sub(r"<[^>]+>", "", text)
    return escape(text)

with open("cherry_prs.json", "w", encoding="utf-8") as f_json:
    json.dump(data, f_json, indent=4, ensure_ascii=False)
print("Arquivo JSON criado: cherry_prs.json")

with open("cherry_prs.csv", "w", newline="", encoding="utf-8") as f_csv:
    writer = csv.DictWriter(f_csv, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
print("Arquivo CSV criado: cherry_prs.csv")

pdf_filename = "cherry_prs.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph(f"<b>Projeto:</b> {repo}", styles["Title"]))
story.append(Spacer(1, 12))
story.append(Paragraph(f"Lista dos últimos {len(data)} Pull Requests fechados", styles["Heading2"]))
story.append(Spacer(1, 12))

for pr in data:
    comments_clean = clean_html(pr['Comments'])
    pr_info = f"""
    <b>PR #{pr['PR_Number']}</b>: {clean_html(pr['PR_Title'])}<br/>
    <b>Autor:</b> {clean_html(pr['Author'])}<br/>
    <b>Criado em:</b> {pr['Created_At']}<br/>
    <b>Fechado em:</b> {pr['Closed_At']}<br/>
    <b>Comentários:</b> {comments_clean[:500]}{'...' if len(comments_clean) > 500 else ''}<br/>
    <b>Estado:</b> {pr['State']}
    """
    story.append(Paragraph(pr_info, styles["Normal"]))
    story.append(Spacer(1, 12))

doc.build(story)
print(f"Arquivo PDF criado: {pdf_filename}")
print("Finalizado com sucesso!")