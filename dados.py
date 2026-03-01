import json
import os

ARQUIVO = "dados.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)
    
def salvar_dados(pessoas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(pessoas, f, indent=4, ensure_ascii=False)