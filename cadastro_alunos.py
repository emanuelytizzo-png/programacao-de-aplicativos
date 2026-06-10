import sqlite3

nome = input("Digite o nome completo do aluno: ")
telefone = input("Digite o telefone: ")
turma = input("Digite a turma: ")
idade = input("Digite a idade: ")
cpf = input("Digite o CPF: ")

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

sql = f"""
insert into alunos (nome_completo, telefone, turma, idade, cpf)
values ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}')
"""

cursor.execute(sql)

conexao.commit()
conexao.close()

 print(f"\n[SUCESSO] Aluno(a) {nome_completo} cadastrado com sucesso!")

except sqlite3.Error as erro:
    print(f"\n[ERRO] Falha ao inserir no banco de dados: {erro}")

finally:

    if conexao:
        conexao.close()
        print("[AVISO] Conexão com o banco de dados fechada com segurança.")


