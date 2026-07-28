import sqlite3 
 
def listar_alunos_e_turmas(): 
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
	# O relatório roda, mas repete os dados erroneamente em formato de matriz cruzada 
	# porque falta definir a regra de colagem (vínculo). Conserte o comando SQL: 
    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas") 
     
	for linha in cursor.fetchall(): 
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}") 
    conexao.close() 

# R= O erro está no comando INNER JOIN, porque ele não possui a cláusula ON, que é responsável por indicar como as tabelas alunos e turmas estão relacionadas. 
# Sem essa condição, o banco combina todos os registros das duas tabelas, gerando dados repetidos.

Correção do código:
import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Lista os alunos junto com suas respectivas turmas
    cursor.execute("""
        SELECT alunos.nome, turmas.nome_turma
        FROM alunos
        INNER JOIN turmas
        ON alunos.id_turma = turmas.id
    """)

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
       
 conexao.close()
