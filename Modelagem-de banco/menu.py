import banco
import escola
import turma
import aluno


def ler_inteiro(mensagem):
    """Lê um número inteiro tratando erros de conversão."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: digite apenas números inteiros.")


def menu_escolas():
    while True:
        print("\n===== MENU ESCOLAS =====")
        print("1 - Cadastrar escola")
        print("2 - Listar escolas")
        print("3 - Alterar escola")
        print("4 - Excluir escola")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da escola: ")
            cidade = input("Cidade: ")
            escola.cadastrar_escola(nome, cidade)

        elif opcao == "2":
            escola.listar_escolas()

        elif opcao == "3":
            id_escola = ler_inteiro("ID da escola: ")
            nome = input("Novo nome: ")
            cidade = input("Nova cidade: ")
            escola.alterar_escola(id_escola, nome, cidade)

        elif opcao == "4":
            id_escola = ler_inteiro("ID da escola: ")
            escola.excluir_escola(id_escola)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_turmas():
    while True:
        print("\n===== MENU TURMAS =====")
        print("1 - Cadastrar turma")
        print("2 - Listar turmas")
        print("3 - Alterar turma")
        print("4 - Excluir turma")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da turma: ")
            id_escola = ler_inteiro("ID da escola: ")
            turma.cadastrar_turma(nome, id_escola)

        elif opcao == "2":
            turma.listar_turmas()

        elif opcao == "3":
            id_turma = ler_inteiro("ID da turma: ")
            nome = input("Novo nome da turma: ")
            id_escola = ler_inteiro("Novo ID da escola: ")
            turma.alterar_turma(id_turma, nome, id_escola)

        elif opcao == "4":
            id_turma = ler_inteiro("ID da turma: ")
            turma.excluir_turma(id_turma)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_alunos():
    while True:
        print("\n===== MENU ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Alterar aluno")
        print("4 - Excluir aluno")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = ler_inteiro("Idade: ")
            id_turma = ler_inteiro("ID da turma: ")
            aluno.cadastrar_aluno(nome, idade, id_turma)

        elif opcao == "2":
            aluno.listar_alunos()

        elif opcao == "3":
            id_aluno = ler_inteiro("ID do aluno: ")
            nome = input("Novo nome: ")
            idade = ler_inteiro("Nova idade: ")
            id_turma = ler_inteiro("Novo ID da turma: ")
            aluno.alterar_aluno(
                id_aluno,
                nome,
                idade,
                id_turma
            )

        elif opcao == "4":
            id_aluno = ler_inteiro("ID do aluno: ")
            aluno.excluir_aluno(id_aluno)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_principal():
    """Executa o menu principal do sistema."""
    banco.criar_tabelas()

    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA DE GESTÃO ESCOLAR")
        print("=" * 40)
        print("1 - Escolas")
        print("2 - Turmas")
        print("3 - Alunos")
        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_escolas()

        elif opcao == "2":
            menu_turmas()

        elif opcao == "3":
            menu_alunos()

        elif opcao == "0":
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
