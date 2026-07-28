import sqlite3 
 
def verificar_registros(): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
    cursor.execute("SELECT * FROM alunos") 
     
	# Por que o segundo print não mostra absolutamente nada no console? 
    print("Primeiro print:", cursor.fetchall()) 
    print("Segundo print:", cursor.fetchall()) 
     
    conexao.close() 

# R= O erro acontece porque o método fetchall() consome todos os registros da consulta na primeira chamada. 
# Quando ele é chamado pela segunda vez, não há mais dados para buscar, por isso o resultado é uma lista vazia.

correção do código:

import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    registros = cursor.fetchall()

    print("Primeiro print:", registros)
    print("Segundo print:", registros)

    conexao.close()