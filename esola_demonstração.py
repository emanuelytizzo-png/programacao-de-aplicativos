import sqlite3import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT,
        salario REAL,
        nome_escola TEXT
    )
    """)
    conexao.commit()

def criar_professor():
    nome = input("Nome Completo: ")
    telefone = input("Telefone: ")
    materia = input("Matéria: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Nome da Escola: ")

    cursor.execute("""
    INSERT INTO professores
    (nome_completo, telefone, materia, idade, cpf, salario, nome_escola)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nome, telefone, materia, idade, cpf, salario, escola))

    conexao.commit()
    print("Professor cadastrado com sucesso!\n") 

 conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    comando = f'''
        INSERT INTO alunos (nome, telefone, turma, idade, cpf, id_professor)
        VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', {id_professor})
    '''

    cursor.execute(comando)
    conexao.commit()
    print("Aluno cadastrado com sucesso!")
    conexao.close()  

def listar():
    print("\n--- Lista de Alunos ---")
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

 cursor.execute("SELECT * FROM alunos")
    todos_alunos = cursor.fetchall()

    if not todos_alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in todos_alunos:
            print(f"ID: {a[0]} | Nome: {a[1]} | Turma: {a[3]} | CPF: {a[5]}")

    conexao.close()

def atualizar():
    print("\n--- Atualizar Dados ---")
    id_busca = int(input("Digite o ID do aluno que deseja editar: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

 cursor.execute(f"SELECT * FROM alunos WHERE id = {id_busca}")
    aluno = cursor.fetchone() 

    if not aluno:
        print("Aluno não encontrado.")
        conexao.close()
        return

    print(f"Editando dados de: {aluno[1]}")
    novo_nome = input(f"Novo Nome ({aluno[1]}): ")
    novo_tel = input(f"Novo Telefone ({aluno[2]}): ")
    nova_turma = input(f"Nova Turma ({aluno[3]}): ")
    nova_idade = input(f"Nova Idade ({aluno[4]}): ")
    novo_cpf = input(f"Novo CPF ({aluno[5]}): ")
    novo_id_professor = int(input(f"Novo ID Professor ({aluno[6]}): "))

    comando = f'''
        UPDATE alunos 
        SET nome = '{novo_nome}', telefone = '{novo_telefone}', turma = '{nova_turma}', 
            idade = {nova_idade}, cpf = '{novo_cpf}', id_professor = {novo_id_professor}
        WHERE id = {id_busca}
    '''
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    print("Dados atualizados com sucesso!")

def excluir():
    print("\n--- Excluir Aluno ---")
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor() 

comando = f"DELETE FROM alunos WHERE id = {id_busca}"
    
    cursor.execute(comando)
    conexao.commit()

    conexao.close()

def menu():
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            turma TEXT,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            id_professor INTEGER,
            FOREIGN KEY (id_professor) REFERENCES professores(id)
        )
    ''')

    conexao.commit()
    conexao.close()

    while True:
        print("\n=== SISTEMA ESCOLAR (SQLITE) ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")


