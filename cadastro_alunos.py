import sqlite3

try:
    nome = input("Digite o nome completo do aluno: ")
    telefone = input("Digite o telefone: ")
    turma = input("Digite a turma: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")

    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()
     sql = f"""
    INSERT INTO alunos (nome_completo, telefone, turma, idade, cpf)
    VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}');
    ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}');
    """

    cursor.execute(sql)
    conexao.commit()

    print("Aluno cadastrado com sucesso!")

    conexao.close()

except Exception as e:
    print(f"Houve um erro ao cadastrar o aluno: {e}")
    

