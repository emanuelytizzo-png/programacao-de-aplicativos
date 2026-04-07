cotacao_dolar = 5.0
valor_reais = float(input("Digite o valor em reais: R$ "))
valor_dolar = valor_reais / cotacao_dolar

print(f"R$ {valor_reais:.2f} equivalem a US$ {valor_dolar:.2f}")