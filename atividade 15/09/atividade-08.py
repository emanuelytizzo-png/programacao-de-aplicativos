def busca_binaria_comparacoes(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if vetor[meio] == valor:
            return meio, comparacoes

        elif valor > vetor[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1, comparacoes


vetor = [1, 3, 5, 7, 9, 11, 13, 15]

posicao, comparacoes = busca_binaria_comparacoes(vetor, 11)

print("Posição:", posicao)
print("Comparações:", comparacoes)
