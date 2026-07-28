import sqlite3 
 
# O aluno criou a conexão fora das funções para "facilitar". 
# Por que isso quebra o sistema quando usamos múltiplos arquivos (módulos)? 
conexao = sqlite3.connect('sistema_escola.db') 
cursor = conexao.cursor() 
 
def inserir_escola(nome): 
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit() 
 
# R= O erro está em criar a conexão e o cursor fora da função.
# Quando o programa é dividido em vários arquivos, essa mesma conexão pode ser compartilhada por diferentes partes do sistema, causando problemas como conexão fechada, 
# conflitos de acesso e dificuldade para gerenciar o banco de dados.

Correção do código:
import sqlite3

def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO escolas (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()