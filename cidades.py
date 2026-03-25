cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome = input("Digite o nome de uma cidade: ")
if nome in cidades:
    posicao = cidades.index(nome)
    print(f"A cidade {nome} está na posição {posicao}.")
else:
    print("Cidade não encontrada na lista.")
