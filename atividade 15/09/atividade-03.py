def maior_numero(vetor):
    maior = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i

    return maior, posicao


vetor = [10, 25, 7, 42, 18, 30]

maior, posicao = maior_numero(vetor)

print("Maior:", maior)
print("Posição:", posicao)
