livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []

livro = input("Digite o nome do livro para empréstimo: ")

if livro in livros_disponiveis:
    livros_disponiveis.remove(livro)
    livros_emprestados.append(livro)
    print("Empréstimo realizado com sucesso!")
else:
    print("Desculpe, este livro não está no acervo.")

livro = input("Digite o nome do livro para devolução: ")

if livro in livros_emprestados:
    livros_emprestados.remove(livro)
    livros_disponiveis.append(livro)
else:
    print("Este livro não consta como emprestado.")

livro = input("Digite o nome do livro para devolução: ")

if livro in livros_emprestados:
    livros_emprestados.remove(livro)
    livros_disponiveis.append(livro)
else:
    print("Este livro não consta como emprestado.")

del livros_disponiveis[0:2]

print("\nEstado final das listas:")
print("Livros disponíveis:", livros_disponiveis)
print("Livros emprestados:", livros_emprestados)
