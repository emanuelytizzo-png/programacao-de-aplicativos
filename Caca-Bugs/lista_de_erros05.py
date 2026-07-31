import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

#Se o usuário digitar "turma B" em vez do número do ID, o sistema quebra.
#o try/except abaixo falhou em capturar esse erro. Qual o problema?
 
 try:
    id_turma = int(input("Digite o ID numérico da turma: ")) 

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
    conexao.commit()
except sqlite3.Error:
    print("Erro no banco de dados!")
finally:
    conexao.close()

#R= Quando o usuário digita um texto no lugar de um número como “turma B” ocorre um erro na tentativa de transformar esse texto em um valor numérico. 
# R= O problema não está no código e sim em como foi escrito pelo usuario. 

correção do código 

import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

    conexao = None

    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect("sistema_escola.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
            (nome, id_turma)
        )

        conexao.commit()

    except ValueError:
        print("Erro: o ID da turma deve ser um número.")

    except sqlite3.Error:
        print("Erro no banco de dados!")

    finally:
        if conexao:
            conexao.close()
