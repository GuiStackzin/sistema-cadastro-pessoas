from cadastro import cadastrar_pessoa
from listagem import listar_pessoas
from dados import carregar_dados, salvar_dados

def menu():
    pessoas = carregar_dados()

    while True:
        print("\n1 - Cadastrar pessoa")
        print("2 - Listar pessoas")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_pessoa(pessoas)
            salvar_dados(pessoas)
        elif opcao == "2":
            listar_pessoas(pessoas)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()