def busca_binaria(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == valor:
            return meio

        elif valor > vetor[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1


vetor = [1, 3, 5, 7, 9, 11, 13, 15]

print(busca_binaria(vetor, 9))