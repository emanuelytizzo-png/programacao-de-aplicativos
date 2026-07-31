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
