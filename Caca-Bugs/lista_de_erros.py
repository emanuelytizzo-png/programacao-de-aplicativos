import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.curso()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL )
    
    ''')

# O banco não está salvando as alterações. por quÊ?

#R= Estava faltando o conexao.commit() para rodar o meu código. 


conexao.commit()
conexao.close()

correção do código:

