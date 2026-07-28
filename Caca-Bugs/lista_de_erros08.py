import sqlite3 
 
def cadastrar_professor(nome, cpf): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 

# O sistema aceita cadastrar dois professores com o mesmo CPF. 
	# Como restringir isso direto na estrutura da tabela abaixo? 
    cursor.execute(''' 
    	CREATE TABLE IF NOT EXISTS professores ( 
        	id INTEGER PRIMARY KEY AUTOINCREMENT, 
        	nome TEXT, 
            cpf TEXT 
        ) 
	''') 

# R=O sistema aceita cadastrar dois professores com o mesmo CPF porque a coluna cpf não possui nenhuma restrição de unicidade. 
# Para impedir isso diretamente na estrutura da tabela, deve-se adicionar a restrição UNIQUE na coluna cpf.

Correção do código:

import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE
        )
    ''')

    try:
        cursor.execute(
            "INSERT INTO professores (nome, cpf) VALUES (?, ?)",
            (nome, cpf)
        )
        conexao.commit()
        print("Professor cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: já existe um professor cadastrado com esse CPF.")
    finally:
        conexao.close()