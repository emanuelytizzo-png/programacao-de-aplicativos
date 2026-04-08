saldo = 500

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor para depósito: R$ "))
        saldo += valor
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: R$ "))
        
        if valor <= saldo:
            saldo -= valor
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente!")
    
    elif opcao == "3":
        print("Encerrando...")
        break
    
    else:
        print("Opção inválida!")