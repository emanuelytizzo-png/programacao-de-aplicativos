def contar_valor(lista, valor):
    contador = 0

    for numero in lista:
        if numero == valor:
            contador += 1

    return contador


lista = [2, 5, 2, 8, 2, 9, 5, 2]

print(contar_valor(lista, 2))
