saldo_inicial = 1000.00
print("1 - deposito, 2 - saque, 3 - extrato. ")
menu = int (input("escolha uma opção: "))

if menu == 1: 
    valor = float(input("digite o valor para depósito: "))
    if valor > 0: 
        saldo_inicial = saldo_inicial + valor 
        print ("deosito realizado com sucesso!")
else: 
    print("valor invalido para deposito. ")

 print