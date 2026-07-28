import sqlite3 
 
def cadastrar_serie_seguro(nome, id_escola): 
    try: 
    	# Se a linha abaixo falhar por falta de permissão na pasta, 
    	# o bloco 'finally' vai tentar fechar algo que não abriu. Como corrigir? 
        conexao = sqlite3.connect('/pasta_protegida/sistema.db') 
    	cursor = conexao.cursor() 
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola)) 
        conexao.commit() 
    except sqlite3.Error as e: 
        print("Erro técnico:", e) 
    finally: 
        conexao.close() 

# R= O erro acontece porque, se a conexão com o banco de dados falhar, a variável conexao não será criada. 
# Mesmo assim, o bloco finally tenta executar conexao.close(), causando outro erro.

correção de código:

import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None

    try:
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
            (nome, id_escola)
        )

        conexao.commit()

    except sqlite3.Error as e:
        print("Erro técnico:", e)

    finally:
        if conexao is not None:
            conexao.close()