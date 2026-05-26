import json
import os

ARQUIVO = "alunos.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON."""
if not os.path.exists(ARQUIVO):
     return []

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
   try:
        return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_dados(alunos):
    """Salva os dados no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

def cadastrar_aluno():
    alunos = carregar_dados()

    try:
        id_digitado = int(input("Digite o ID do aluno: "))
    except ValueError:
        print("Erro: O ID deve ser um número inteiro!")
        return

    for aluno in alunos:
    if aluno["id"] == id_digitado:
            print("Erro: Este ID já está em uso!")
            return

    novo_aluno = {
        "id": id_digitado,
        "nome": input("Nome Completo: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": input("Idade: "),
        "cpf": input("CPF: ")
    }

  alunos.append(novo_aluno)
    salvar_dados(alunos)

    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    alunos = carregar_dados()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
