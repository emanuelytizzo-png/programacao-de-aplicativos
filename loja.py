valor_total = float(input("digite o valor total: "))
cumpom = (input("digite o cumpom: "))

desconto = valor_total * 0.10 
novo_preço = valor_total - desconto 

if cumpom == "DEV10":
    print("cumpom valido" , novo_preço)

else:
    print("cumpom invalido" , valor_total)