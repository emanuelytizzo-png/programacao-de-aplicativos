itens = []

while True:
    print("\n1 - Adicionar")
    print("2 - Listar")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        itens.append(item)
        print("Item adicionado!")

    elif opcao == "2":
        print("Lista de itens:")
        for i in itens:
            print("-", i)

    elif opcao == "3":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")