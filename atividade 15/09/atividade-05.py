def primeira_ultima(vetor, valor):
    primeira = -1
    ultima = -1

    for i in range(len(vetor)):
        if vetor[i] == valor:
            if primeira == -1:
                primeira = i

            ultima = i

    return primeira, ultima


vetor = [5, 2, 8, 2, 9, 2, 4, 7]

primeira, ultima = primeira_ultima(vetor, 2)

print("Primeira posição:", primeira)
print("Última posição:", ultima)
