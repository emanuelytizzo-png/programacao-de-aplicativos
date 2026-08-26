import sqlite3


def conectar():
    return sqlite3.connect("petshop.db")


def criar():
    nome = input("Nome do pet: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    id_cliente = input("ID do dono: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO pets
        (nome, especie, raca, idade, id_cliente)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nome, especie, raca, idade, id_cliente)
    )

    conexao.commit()
    conexao.close()

    print("Pet cadastrado com sucesso!")


def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pets")

    pets = cursor.fetchall()

    conexao.close()

    print("\n===== LISTA DE PETS =====")

    for pet in pets:
        print(
            f"ID: {pet[0]} | "
            f"Nome: {pet[1]} | "
            f"Espécie: {pet[2]} | "
            f"Raça: {pet[3]} | "
            f"Idade: {pet[4]} | "
            f"ID Dono: {pet[5]}"
        )


def alterar():
    id_pet = input("Digite o ID do pet: ")
    nome = input("Novo nome: ")
    especie = input("Nova espécie: ")
    raca = input("Nova raça: ")
    idade = input("Nova idade: ")
    id_cliente = input("Novo ID do dono: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        UPDATE pets
        SET nome = ?,
            especie = ?,
            raca = ?,
            idade = ?,
            id_cliente = ?
        WHERE id = ?
        """,
        (nome, especie, raca, idade, id_cliente, id_pet)
    )

    conexao.commit()
    conexao.close()

    print("Pet alterado com sucesso!")


def excluir():
    id_pet = input("Digite o ID do pet: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM pets WHERE id = ?",
        (id_pet,)
    )

    conexao.commit()
    conexao.close()

    print("Pet excluído com sucesso!")
