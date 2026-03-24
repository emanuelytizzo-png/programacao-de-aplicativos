autorizados = ["Alice", "Bob", "Carlos"]
nome = input("Digite o nome do pesquisador: ")
if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")
    
remover = input(f"Deseja remover {nome} da lista? (Sim/Não): ").capitalize()
    if remover == "Sim":
        autorizados.remove(nome)
        print(f"Lista atualizada: {autorizados}")
    else: 
        print("Lista inalterada.")
else:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")

  cadastrar = input(f"Deseja cadastrar {nome} na lista? (Sim/Não): ").capitalize()
    if cadastrar == "Sim":
        autorizados.append(nome)
        print(f"Lista final: {autorizados}")
    else:
        print(f"Lista final: {autorizados}")