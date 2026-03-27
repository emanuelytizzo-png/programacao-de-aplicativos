compras = []
while True:
    produto = input("Digite um produto (ou 'fim' para encerrar): ")
    
    if produto.lower() == "fim":
        break
    
    compras.append(produto)
print("\nLista de compras:")
for item in compras:
    print(item)