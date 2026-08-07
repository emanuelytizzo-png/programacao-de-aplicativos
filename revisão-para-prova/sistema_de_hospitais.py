import sqlite3

conexao = sqlite3.connect("hospital.db")
cursor = conexao.cursor()

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
    """)

 conexao.commit()
    print("Tabelas criadas com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao criar tabelas:", erro)


def cadastrar_hospital():
    nome = input("Nome do hospital: ")
    cidade = input("Cidade: ")

    cursor.execute(
        "INSERT INTO hospitais (nome, cidade) VALUES (?, ?)",
        (nome, cidade)
    )
    conexao.commit()
    print("Hospital cadastrado com sucesso!\n")

    def cadastrar_medico():
    nome = input("Nome do médico: ")
    crm = input("CRM: ")
    id_hospital = int(input("ID do hospital: "))

    cursor.execute(
        "SELECT * FROM hospitais WHERE id = ?",
        (id_hospital,)
    )

    hospital = cursor.fetchone()

    if hospital is None:
        print("Erro: Hospital não encontrado!\n")
        return

    cursor.execute(
        """
        INSERT INTO medicos (nome, crm, id_hospital)
        VALUES (?, ?, ?)
        """,
        (nome, crm, id_hospital)
    )

    conexao.commit()
    print("Médico cadastrado com sucesso!\n")

    while True:
    print("1 - Cadastrar Hospital")
    print("2 - Cadastrar Médico")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_hospital()

    elif opcao == "2":
        cadastrar_medico()

    elif opcao == "3":
        break

    else:
        print("Opção inválida!\n")

conexao.close()
