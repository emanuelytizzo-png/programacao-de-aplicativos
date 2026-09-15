def busca_sequencial_comparacoes(vetor, valor):
    comparacoes = 0

    for i in range(len(vetor)):
        comparacoes += 1

        if vetor[i] == valor:
            return i, comparacoes

    return -1, comparacoes


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

vetor = list(range(1, 101))

valores = [10, 50, 100]

for valor in valores:
    pos_seq, comp_seq = busca_sequencial_comparacoes(vetor, valor)
    pos_bin, comp_bin = busca_binaria_comparacoes(vetor, valor)

    print("Valor:", valor)
    print("Busca sequencial - posição:", pos_seq,
          "- comparações:", comp_seq)
    print("Busca binária - posição:", pos_bin,
          "- comparações:", comp_bin)
    print()
