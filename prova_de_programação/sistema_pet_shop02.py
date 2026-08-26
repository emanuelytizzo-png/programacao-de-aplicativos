import sqlite3


def conectar():
    return sqlite3.connect("petshop.db")


def criar():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO clientes (nome, telefone, email)
        VALUES (?, ?, ?)
        """,
        (nome, telefone, email)
    )

    conexao.commit()
    conexao.close()

    print("Cliente cadastrado com sucesso!")


def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    conexao.close()

    print("\n===== LISTA DE CLIENTES =====")

    for cliente in clientes:
        print(
            f"ID: {cliente[0]} "
            f"Nome: {cliente[1]} "
            f"Telefone: {cliente[2]} "
            f"E-mail: {cliente[3]}"
        )


def alterar():
    id_cliente = input("Digite o ID do cliente: ")
    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    email = input("Novo e-mail: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE clientes
        SET nome = ?, telefone = ?, email = ?
        WHERE id = ?
        """,
        (nome, telefone, email, id_cliente)
    )

    conexao.commit()
    conexao.close()

    print("Cliente alterado com sucesso!")


def excluir():
    id_cliente = input("Digite o ID do cliente: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id_cliente,)
    )

    conexao.commit()
    conexao.close()

    print("Cliente excluído com sucesso!")
