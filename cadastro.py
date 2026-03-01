def cadastrar_pessoa(pessoas):
    nome = input("Digite o nome: ")

    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0 or idade > 150:
                print("Idade inválida.")
            else:
                break
        except ValueError:
            print("Digite um número válido.")

    pessoas.append({
        "nome": nome,
        "idade": idade
    })

    print("Pessoa cadastrada com sucesso!")