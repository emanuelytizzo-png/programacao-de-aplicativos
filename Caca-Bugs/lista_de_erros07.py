import sqlite3 
 
def cadastrar_turma(nome, id_serie, id_prof): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
    cursor.execute("PRAGMA foreign_keys = ON;") 

# O Python reclama de "Incorrect number of bindings".  
	# Estamos passando a variável, por que ocorre o erro? 
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof)) 
	resultado = cursor.fetchone() 
	print(resultado) 
    conexao.close() 

#R=Se ocorrer um IntegrityError durante o INSERT, a execução é interrompida e a linha conexao.close() não é executada. Como consequência, a conexão pode permanecer aberta. co

correção do código:

import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute(
            "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",
            (nome, id_serie, id_prof)
        )
        conexao.commit()
        print("Turma cadastrada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: o professor informado não existe.")
    finally:
        conexao.close() 
