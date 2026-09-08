import sqlite3

NOME_BANCO = "gestao_escolar.db"


def conectar():
    """Cria uma conexão com o banco e ativa as chaves estrangeiras."""
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao


def criar_tabelas():
    """Cria as tabelas do sistema caso elas ainda não existam."""
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS turmas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                id_escola INTEGER NOT NULL,
                FOREIGN KEY (id_escola)
                    REFERENCES escolas(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_turma INTEGER NOT NULL,
                FOREIGN KEY (id_turma)
                    REFERENCES turmas(id)
            )
        """)

        conexao.commit()
        conexao.close()

    except sqlite3.Error as erro:
        print(f"Erro ao criar as tabelas: {erro}")
