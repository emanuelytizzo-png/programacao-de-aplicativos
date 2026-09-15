def busca_sequencial(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return -1


vetor = [4, 7, 2, 9, 1, 8, 5, 3, 6, 10]

print(busca_sequencial(vetor, 8))
