from classificacao import classificacao_por_idade

def listar_pessoas(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return

    for i, pessoa in enumerate(pessoas, 1):
        classificacao = classificacao_por_idade(pessoa["idade"])
        print(f"{i}. {pessoa['nome']} | {pessoa['idade']} | {classificacao}")