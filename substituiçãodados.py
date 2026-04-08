nomes = ["Amanda", "Carolina", "Bernado", "Maria"]

antigo = input("Digite o nome que deseja alterar: ")
novo = input("Digite o novo nome: ")

for i in range(len(nomes)):
    if nomes[i] == antigo:
        nomes[i] = novo
        print("Nome alterado com sucesso!")
        break
else:
    print("Nome não encontrado.")

print("Lista atualizada:", nomes)
