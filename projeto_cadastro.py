def cadastrar_pessoa(pessoas):
    """Função para cadastrar uma nova pessoa"""
    print("\n--- CADASTRO DE PESSOA ---")
    nome = input("Digite o nome: ")
    
    # Validação da idade
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0 or idade > 150:
                print("Idade inválida! Digite uma idade entre 0 e 150.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido para idade.")
    
    # Adiciona a pessoa à lista
    pessoas.append({'nome': nome, 'idade': idade})
    print(f"Pessoa cadastrada com sucesso!")

def listar_pessoas(pessoas):
    """Função para listar todas as pessoas cadastradas"""
    print("\n--- LISTA DE PESSOAS CADASTRADAS ---")
    
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    
    for i, pessoa in enumerate(pessoas, 1):
        # Determina a classificação da pessoa
        classificacao = classificar_por_idade(pessoa['idade'])
        print(f"{i}. Nome: {pessoa['nome']:<20} | Idade: {pessoa['idade']:3} | {classificacao}")

def classificar_por_idade(idade):
    """Função para classificar uma pessoa baseado na idade"""
    if idade < 18:
        return "Menor de idade"
    elif idade >= 65:
        return "Aposentável"
    else:
        return "Em idade ativa"

def classificar_lista(pessoas):
    """Função para listar pessoas por classificação"""
    print("\n--- LISTA POR CLASSIFICAÇÃO ---")
    
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    
    # Agrupa pessoas por classificação
    menores = []
    ativos = []
    aposentados = []
    
    for pessoa in pessoas:
        if pessoa['idade'] < 18:
            menores.append(pessoa)
        elif pessoa['idade'] >= 65:
            aposentados.append(pessoa)
        else:
            ativos.append(pessoa)
    
    # Mostra menores de idade
    print("\n--- MENORES DE IDADE ---")
    if menores:
        for pessoa in menores:
            print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")
    else:
        print("Nenhum menor de idade cadastrado.")
    
    # Mostra em idade ativa
    print("\n--- EM IDADE ATIVA ---")
    if ativos:
        for pessoa in ativos:
            print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")
    else:
        print("Nenhuma pessoa em idade ativa cadastrada.")
    
    # Mostra aposentáveis
    print("\n--- APOSENTÁVEIS ---")
    if aposentados:
        for pessoa in aposentados:
            print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")
    else:
        print("Nenhum aposentável cadastrado.")

def menu():
    """Função principal que controla o menu do programa"""
    pessoas = []  # Lista para armazenar as pessoas cadastradas
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE CADASTRO DE PESSOAS")
        print("="*50)
        print("1. Cadastrar pessoa")
        print("2. Listar todas as pessoas")
        print("3. Listar por classificação")
        print("4. Sair")
        print("-"*50)
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            cadastrar_pessoa(pessoas)
        
        elif opcao == "2":
            listar_pessoas(pessoas)
        
        elif opcao == "3":
            classificar_lista(pessoas)
        
        elif opcao == "4":
            print("\nSaindo do sistema...")
            print("Obrigado por utilizar o programa!")
            break
        
        else:
            print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 4.")

# Execução do programa
if __name__ == "__main__":
    menu()