import sqlite3

def conectar_banco():
    conexao = sqlite3.connect('sistema_petshop.db')
    conexao.execute('PRAGMA foreign_keys = ON')
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS redes_pet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_rede TEXT NOT NULL,
        site TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lojas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bairro TEXT NOT NULL,
        id_rede INTEGER NOT NULL,
        FOREIGN KEY (id_rede) REFERENCES redes_pet(id)
    )
    ''')
    conexao.commit()
    conexao.close()

def inserir_rede(nome_rede, site):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO redes_pet (nome_rede, site) VALUES (?, ?)
    ''', (nome_rede, site))
    conexao.commit()
    conexao.close()

def inserir_loja(bairro, id_rede):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO lojas (bairro, id_rede) VALUES (?, ?)
    ''', (bairro, id_rede))
    conexao.commit()
    conexao.close()

def listar_redes_pet():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM redes_pet')
    redes = cursor.fetchall()
    for rede in redes:
        print(rede)
    conexao.close()

def listar_lojas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM lojas')
    lojas = cursor.fetchall()
    for loja in lojas:
        print(loja)
    conexao.close()

criar_tabelas()

inserir_rede('Pet Mania', '://petmania.com.br')
inserir_rede('Mundo Pet', '://mundopet.com.br')

inserir_loja('Centro', 1)
inserir_loja('Batel', 1)
inserir_loja('Água Verde', 2)

print('Redes de Pet Shop:')
listar_redes_pet()

print('\nLojas:')
listar_lojas()
