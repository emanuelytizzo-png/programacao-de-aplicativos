open('viagens.txt', 'w').close()

def criar():
    nome = input("Nome dos viajantes: ")
    with open('viajantes.txt', 'a') as f:
       f.write(nome + '\n')
    print("local adicionado!")

def ler():
    with open('viagem.txt', 'r') as f:
        viagem = f.readlines()

   i = 0
        for viagem in viagem:
            print(f"{i} - {viagem.strip()}") 

def atualizar():
    ler() 
    idx = int(input("Digite o ID do viajante que deseja alterar: "))
    novo_nome = input("Novo nome: ")
    
    with open('viajante.txt', 'r') as f:
        linhas = f.readlines()

with open('viajante.txt', 'r') as f:
        linhas = f.readlines()
    
    linhas[idx] = novo_nome + '\n' 
    
    with open('vijante.txt', 'w') as f: 
        f.writelines(linhas)
    print("viajante atualizado!")

def deletar():
    ler()
    idx = int(input("Digite o ID do viajante que deseja excluir: "))
    
    with open('viagem.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx]
    
    with open('viagem.txt', 'w') as f:
        f.writelines(linhas)
    print("Aluno removido!")


while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
     opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break 

