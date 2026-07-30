import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
    	cursor = conexao.cursor() 
    	# Existe um erro de digitação no comando SQL (INSERTO).  
    	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
        cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 
    finally: 
        conexao.close() 

# R= O erro acontece porque o comando SQL foi escrito incorretamente como INSERTO, quando o correto é INSERT. Isso gera um erro de sintaxe no SQL.
# No entanto, o programa exibe a mensagem "CPF já está cadastrado no sistema!" porque o bloco except sqlite3.
# Error captura qualquer erro do SQLite, incluindo erros de sintaxe e não apenas erros de CPF duplicado.

correção do código:

import sqlite3 

def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor()

   cursor.execute( 
    "INSERT INTO professores (nome, materia, cpf) VALUES (?, ?, ?)", 
    (nome, materia, cpf)
    
    )     

conexao.commit()

except sqlite3.IntegrityError: 
    print("Erro: Este CPF já está cadastrado no sistema!")

    except sqlite3.Error as erro: 
        print("Erro no banco de dados:", erro)

        finally: 
            conexao.close()

