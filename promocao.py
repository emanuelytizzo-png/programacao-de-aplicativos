valor = float (input("digite o valor da compra: "))
prime = input("voce tem prime? s/n?") 
frete = 50.00

if (valor >= 50.00 or prime == "s") and valor > 100.00:
    frete == 00.00
    print ("voce nao ganhou frete gratis")
    valor_total = valor = frete
    print ("seu valor é" , valor_frete)

else:
    frete = 50.00
    valor_total = valor + frete 
    print("voce nao ganhou frete gratis")
    print("seu valor total é" , valor_total)
    