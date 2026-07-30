import sqlite3 
 
def cadastrar_lista_alunos(): 
	lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 
     
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
	# O comando executemany quebra com a mensagem: "function takes exactly 2 arguments". 
	# Como passar a lista de dados da forma correta dentro dele? 
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista) 
     
    conexao.commit() 
    conexao.close() 
 
# R= O erro acontece porque foi utilizado o comando cursor.execute() para inserir vários registros de uma só vez.
# O método execute() aceita apenas um conjunto de valores, enquanto a variável lista contém vários registros.
# Para inserir vários dados ao mesmo tempo, é necessário usar o método cursor.executemany(), passando primeiro o comando SQL e depois a lista de tuplas com os valores.

correção de código:

import sqlite3

def cadastrar_lista_alunos(): 
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)]

    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()

    cursor.executemany( 
        "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", 
        lista 
        )

        conexao.commit() 
        conexao.close()