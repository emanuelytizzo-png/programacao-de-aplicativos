import sqlite3 
 
def cadastrar_escola_manual(): 
	# O aluno resolveu gerar o ID por conta própria 
    id_escola = int(input("Digite o ID para a nova escola: ")) 
	nome = input("Nome da escola: ") 
     
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
	# Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash). 
	# Aplique a blindagem protetora necessária: 
    cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
     
    conexao.commit() 
    conexao.close() 

# R= O erro acontece porque o usuário informa o id manualmente.
# Se ele tentar cadastrar uma escola usando um id que já existe, o SQLite gera um erro de chave primária duplicada (IntegrityError) e o programa encerra de forma inesperada.

correção de código:

import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: ")) 
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect("sistema_escola.db") 
    cursor = conexao.cursor()

    try:
        cursor.execute( 
            "INSERT INTO escolas (id, nome) VALUES (?, ?)", 
        (id_escola, nome)

          )
        conexao.commit() 
        print("Escola cadastrada com sucesso!")

        except sqlite3.IntegrityError: 
            print("Erro: já existe uma escola cadastrada com esse ID.")

        finally:
        conexao.close()
