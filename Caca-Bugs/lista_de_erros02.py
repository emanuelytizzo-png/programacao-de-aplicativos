import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

#O aluno tenta cadastraruma série com id_escola = 999 (que não existe).
#O SQLite aceita o cadastro mesmo assim. o que está faltando ativar?

try:
    cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
    (nome_serie, id_escola)) 
            conexao.commit()
       except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!") 
        finally:
            conexao.close()


#R= Estava faltando ativar  PRAGMA foreign_keys = ON.

correção do código:

import sqlite3 
def cadastrar_serie(nome_serie, id_escola): 
    conexao = sqlite3.connect('sistema_escola.db') 
    conexao.execute("PRAGMA foreign_keys = ON") 
    cursor = conexao.cursor()

try:
    cursor.execute(
        "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
        (nome_serie, id_escola)
        
         )

conexao.commit()

except sqlite3.IntegrityError:
    print("Erro: Escola inexistente!")

finally: 
    conexao.close()