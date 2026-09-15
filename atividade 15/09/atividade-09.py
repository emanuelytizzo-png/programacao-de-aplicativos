def posicao_insercao(vetor, valor):
    inicio = 0
    fim = len(vetor)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if vetor[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio

    return inicio


vetor = [10, 20, 30, 40, 50]

print(posicao_insercao(vetor, 35))

