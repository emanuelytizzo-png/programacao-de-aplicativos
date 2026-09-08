import sqlite3
from banco import conectar


def cadastrar_escola(nome, cidade):
    """Cadastra uma nova escola."""
    try:
        nome = nome.strip()
        cidade = cidade.strip()

        assert nome != "", "O nome da escola não pode ser vazio."
        assert cidade != "", "A cidade não pode ser vazia."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO escolas (nome, cidade)
            VALUES (?, ?)
        """, (nome, cidade))

        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_escolas():
    """Lista todas as escolas."""
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        conexao.close()

        print("\n--- ESCOLAS ---")

        if not escolas:
            print("Nenhuma escola cadastrada.")
            return

        for escola in escolas:
            print(
                f"ID: {escola[0]} | "
                f"Nome: {escola[1]} | "
                f"Cidade: {escola[2]}"
            )

    except sqlite3.Error as erro:
        print(f"Erro ao listar escolas: {erro}")


def alterar_escola(id_escola, nome, cidade):
    """Altera os dados de uma escola."""
    try:
        nome = nome.strip()
        cidade = cidade.strip()

        assert id_escola > 0, "O ID da escola deve ser maior que zero."
        assert nome != "", "O nome da escola não pode ser vazio."
        assert cidade != "", "A cidade não pode ser vazia."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE escolas
            SET nome = ?, cidade = ?
            WHERE id = ?
        """, (nome, cidade, id_escola))

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            conexao.commit()
            print("Escola alterada com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def excluir_escola(id_escola):
    """Exclui uma escola."""
    try:
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM escolas WHERE id = ?",
            (id_escola,)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            conexao.commit()
            print("Escola excluída com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível excluir a escola. "
            "Existem turmas vinculadas a ela."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
