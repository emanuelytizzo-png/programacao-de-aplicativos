def procurar_aluno(alunos, nome):
    for aluno in alunos:
        if aluno == nome:
            return True

    return False


alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]

if procurar_aluno(alunos, "Maria"):
    print("Aluno encontrado!")
else:
    print("Aluno não encontrado!")