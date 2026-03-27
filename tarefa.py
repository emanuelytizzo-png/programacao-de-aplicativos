ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]
busca = input("Digite o nome da ferramenta que você está procurando: ")

encontrado = False 
for indice, ferramenta in enumerate(ferramentas):
    if busca.lower() == ferramenta.lower():
        print(f"Peça encontrada na posição {indice}!")
        encontrado = True
        break
if not encontrado:
    print("Peça não encontrada.")
while True:
        resposta = input("Deseja adicionar essa ferramenta à lista? (s/n): ").lower()
      