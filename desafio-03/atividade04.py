matriculas = [502, 101, 999, 304, 205, 110]

for i in range(len(matriculas)):
    menor = i

    for j in range(i + 1, len(matriculas)):
        if matriculas[j] < matriculas[menor]:
            menor = j

    matriculas[i], matriculas[menor] = matriculas[menor], matriculas[i]


print("Matrículas ordenadas:", matriculas)

resultado = busca_binaria(matriculas, 205)

print("Posição da matrícula 205:", resultado)
