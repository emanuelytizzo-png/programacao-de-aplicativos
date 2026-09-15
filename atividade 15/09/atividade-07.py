def buscar_palavra(palavras, palavra):
    inicio = 0
    fim = len(palavras) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if palavras[meio] == palavra:
            return True

        elif palavra > palavras[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    return False


palavras = ["ana", "bruno", "carlos", "joao", "maria", "pedro"]

print(buscar_palavra(palavras, "maria"))
