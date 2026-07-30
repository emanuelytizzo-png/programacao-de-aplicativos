def menu(): 
	while True: 
        print("1. Cadastrar Aluno") 
        print("2. Sair") 
        opcao = input("Escolha: ") 
         
        if opcao == "1": 
            print("Cadastrando...") 
        elif opcao == "2": 
            print("Saindo do programa.") 
        	# Por que o programa continua rodando e mostrando o menu mesmo digitando 2? 
            pass 

# R= O erro acontece porque, quando o usuário escolhe a opção "2", o programa apenas imprime a mensagem "Saindo do programa.", 
# mas não existe nenhum comando para encerrar o laço while True.

correção do código:

def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()