import sqlite3
from banco import conectar


def cadastrar_turma(nome_turma, id_escola):
    """Cadastra uma turma vinculada a uma escola."""
    try:
        nome_turma = nome_turma.strip()

        assert nome_turma != "", "O nome da turma não pode ser vazio."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO turmas (nome_turma, id_escola)
            VALUES (?, ?)
        """, (nome_turma, id_escola))

        conexao.commit()
        conexao.close()

        print("Turma cadastrada com sucesso!")

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Erro: a escola informada não existe. "
            "Informe um ID de escola válido."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_turmas():
    """Lista todas as turmas."""
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        conexao.close()

        print("\n--- TURMAS ---")

        if not turmas:
            print("Nenhuma turma cadastrada.")
            return

        for turma in turmas:
            print(
                f"ID: {turma[0]} | "
                f"Nome: {turma[1]} | "
                f"ID Escola: {turma[2]}"
            )

    except sqlite3.Error as erro:
        print(f"Erro ao listar turmas: {erro}")


def alterar_turma(id_turma, nome_turma, id_escola):
    """Altera os dados de uma turma."""
    try:
        nome_turma = nome_turma.strip()

        assert id_turma > 0, "O ID da turma deve ser maior que zero."
        assert nome_turma != "", "O nome da turma não pode ser vazio."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
        """, (nome_turma, id_escola, id_turma))

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            conexao.commit()
            print("Turma alterada com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Erro: a escola informada não existe. "
            "Informe um ID de escola válido."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def excluir_turma(id_turma):
    """Exclui uma turma."""
    try:
        assert id_turma > 0, "O ID da turma deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM turmas WHERE id = ?",
            (id_turma,)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            conexao.commit()
            print("Turma excluída com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível excluir a turma. "
            "Existem alunos vinculados a ela."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
 