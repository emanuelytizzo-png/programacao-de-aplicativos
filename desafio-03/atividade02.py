alunos = ["Pedro", "Ana", "Lucas", "Beatriz", "Carlos"]

for i in range(len(alunos)):
    for j in range(0, len(alunos) - i - 1):

        if alunos[j] > alunos[j + 1]:
            alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]

            print("Troca realizada:", alunos)

print("Lista final ordenada:", alunos)
