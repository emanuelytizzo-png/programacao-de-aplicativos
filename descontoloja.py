preco = float(input("Digite o valor da compra: R$ "))

if preco > 100:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f"Valor com desconto: R$ {preco_final:.2f}")
else:
    print(f"Valor normal: R$ {preco:.2f}")