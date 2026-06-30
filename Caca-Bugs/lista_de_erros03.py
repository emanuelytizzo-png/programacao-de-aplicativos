import sqlite3
 
def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

#Este bloco quebra ao rodar pela primeira vez em um banco limpo. por que?
cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT 
    )
    ''')
     conexao.commit()
     conexao.close()

#R= A tabela não existe então meu código não ira rodar pós o repositorio está vazio então não será possivel rodar.

coreção do código:



