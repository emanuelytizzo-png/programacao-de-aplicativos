import sqlite3

def conectar():
    try:
        conexao = sqlite3.connect("petshop.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao
    except sqlite3.Error as erro:
        print("Erro ao conectar ao banco:", erro)
        return None

def criar_tabelas():
    try:
        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT NOT NULL,
                raca TEXT NOT NULL,
                cliente_id INTEGER NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        """)

        conexao.commit()
        conexao.close()
    except sqlite3.Error as erro:
        print("Erro ao criar tabelas:", erro)

def cadastrar_cliente():
    try:
        nome = input("Nome do cliente: ").strip()
        telefone = input("Telefone: ").strip()

        if not nome or not telefone:
            print("Preencha todos os campos.")
            return

        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, telefone) VALUES (?, ?)",
            (nome, telefone)
        )

        conexao.commit()
        conexao.close()

        print("Cliente cadastrado com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar cliente:", erro)
    except ValueError:
        print("Entrada inválida.")

def listar_clientes():
    try:
        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone FROM clientes")

        clientes = cursor.fetchall()
        conexao.close()

        if not clientes:
            print("Nenhum cliente cadastrado.")
            return

        print("\n--- CLIENTES ---")

        for cliente in clientes:
            print(
                "ID:", cliente[0],
                "| Nome:", cliente[1],
                "| Telefone:", cliente[2]
            )
    except sqlite3.Error as erro:
        print("Erro ao listar clientes:", erro)

def atualizar_cliente():
    try:
        id_cliente = int(input("ID do cliente: "))
        nome = input("Novo nome: ").strip()
        telefone = input("Novo telefone: ").strip()

        if not nome or not telefone:
            print("Preencha todos os campos.")
            return

        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE clientes SET nome = ?, telefone = ? WHERE id = ?",
            (nome, telefone, id_cliente)
        )

        if cursor.rowcount == 0:
            print("Cliente não encontrado.")
        else:
            conexao.commit()
            print("Cliente atualizado com sucesso.")

        conexao.close()
    except sqlite3.Error as erro:
        print("Erro ao atualizar cliente:", erro)
    except ValueError:
        print("Digite um ID válido.")

def excluir_cliente():
    try:
        id_cliente = int(input("ID do cliente: "))

        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM pets WHERE cliente_id = ?",
            (id_cliente,)
        )

        pets = cursor.fetchall()

        if pets:
            print("Não é possível excluir o cliente porque existem pets cadastrados para ele.")
            conexao.close()
            return

        cursor.execute(
            "DELETE FROM clientes WHERE id = ?",
            (id_cliente,)
        )

        if cursor.rowcount == 0:
            print("Cliente não encontrado.")
        else:
            conexao.commit()
            print("Cliente excluído com sucesso.")

        conexao.close()
    except sqlite3.Error as erro:
        print("Erro ao excluir cliente:", erro)
    except ValueError:
        print("Digite um ID válido.")

def cadastrar_pet():
    try:
        nome = input("Nome do pet: ").strip()
        especie = input("Espécie: ").strip()
        raca = input("Raça: ").strip()
        cliente_id = int(input("ID do cliente responsável: "))

        if not nome or not especie or not raca:
            print("Preencha todos os campos.")
            return

        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM clientes WHERE id = ?",
            (cliente_id,)
        )

        cliente = cursor.fetchone()

        if cliente is None:
            print("Cliente não encontrado. Cadastre o cliente primeiro.")
            conexao.close()
            return

        cursor.execute(
            """
            INSERT INTO pets (nome, especie, raca, cliente_id)
            VALUES (?, ?, ?, ?)
            """,
            (nome, especie, raca, cliente_id)
        )

        conexao.commit()
        conexao.close()

        print("Pet cadastrado com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar pet:", erro)
    except ValueError:
        print("Digite um ID válido.")

def listar_pets():
    try:
        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT pets.id, pets.nome, pets.especie, pets.raca,
                   clientes.nome
            FROM pets
            INNER JOIN clientes ON pets.cliente_id = clientes.id
        """)

        pets = cursor.fetchall()
        conexao.close()

        if not pets:
            print("Nenhum pet cadastrado.")
            return

        print("\n--- PETS ---")

        for pet in pets:
            print(
                "ID:", pet[0],
                "| Nome:", pet[1],
                "| Espécie:", pet[2],
                "| Raça:", pet[3],
                "| Dono:", pet[4]
            )
    except sqlite3.Error as erro:
        print("Erro ao listar pets:", erro)

def atualizar_pet():
    try:
        id_pet = int(input("ID do pet: "))
        nome = input("Novo nome: ").strip()
        especie = input("Nova espécie: ").strip()
        raca = input("Nova raça: ").strip()
        cliente_id = int(input("Novo ID do cliente: "))

        if not nome or not especie or not raca:
            print("Preencha todos os campos.")
            return

        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM clientes WHERE id = ?",
            (cliente_id,)
        )

        cliente = cursor.fetchone()

        if cliente is None:
            print("Cliente não encontrado.")
            conexao.close()
            return

        cursor.execute(
            """
            UPDATE pets
            SET nome = ?, especie = ?, raca = ?, cliente_id = ?
            WHERE id = ?
            """,
            (nome, especie, raca, cliente_id, id_pet)
        )

        if cursor.rowcount == 0:
            print("Pet não encontrado.")
        else:
            conexao.commit()
            print("Pet atualizado com sucesso.")

        conexao.close()
    except sqlite3.Error as erro:
        print("Erro ao atualizar pet:", erro)
    except ValueError:
        print("Digite valores válidos.")

def excluir_pet():
    try:
        id_pet = int(input("ID do pet: "))

        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM pets WHERE id = ?",
            (id_pet,)
        )

        if cursor.rowcount == 0:
            print("Pet não encontrado.")
        else:
            conexao.commit()
            print("Pet excluído com sucesso.")

        conexao.close()
    except sqlite3.Error as erro:
        print("Erro ao excluir pet:", erro)
    except ValueError:
        print("Digite um ID válido.")

def menu():
    try:
        criar_tabelas()

        while True:
            print("\n========== PET SHOP ==========")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Atualizar cliente")
            print("4 - Excluir cliente")
            print("5 - Cadastrar pet")
            print("6 - Listar pets")
            print("7 - Atualizar pet")
            print("8 - Excluir pet")
            print("0 - Sair")
            print("==============================")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_cliente()
            elif opcao == "2":
                listar_clientes()
            elif opcao == "3":
                atualizar_cliente()
            elif opcao == "4":
                excluir_cliente()
            elif opcao == "5":
                cadastrar_pet()
            elif opcao == "6":
                listar_pets()
            elif opcao == "7":
                atualizar_pet()
            elif opcao == "8":
                excluir_pet()
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida.")
    except Exception as erro:
        print("Erro no sistema:", erro)

menu()
