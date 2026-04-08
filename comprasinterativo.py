produtos = []

while True:
    item = input("Digite um produto (ou 'sair' para encerrar): ")
    
    if item.lower() == "sair":
        break
    
    produtos.append(item)

print("Lista de produtos:", produtos)