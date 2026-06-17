import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT,
        salario REAL,
        nome_escola TEXT
    )
    """)
    conexao.commit()
    def criar_professor():
    nome = input("Nome Completo: ")
    telefone = input("Telefone: ")
    materia = input("Matéria: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Nome da Escola: ")

    cursor.execute("""
    INSERT INTO professores
    (nome_completo, telefone, materia, idade, cpf, salario, nome_escola)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nome, telefone, materia, idade, cpf, salario, escola))

    conexao.commit()
    print("Professor cadastrado com sucesso!\n")

