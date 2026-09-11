def listar_alunos():
    conn = sqlite3.connect("escola.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos ORDER BY nome ASC")
    alunos = cursor.fetchall()

    for aluno in alunos:
        print(aluno)

    conn.close()

numeros = list(range(1, 101))


def busca_sequencial(lista, valor):
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1

        if lista[i] == valor:
            print(f"Busca Sequencial: valor encontrado na posição {i}")
            print(f"Comparações realizadas: {comparacoes}")
            return i

    print("Valor não encontrado.")
    print(f"Comparações realizadas: {comparacoes}")
    return -1


def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == valor:
            print(f"Busca Binária: valor encontrado na posição {meio}")
            print(f"Comparações realizadas: {comparacoes}")
            return meio

        elif lista[meio] < valor:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("Valor não encontrado.")
    print(f"Comparações realizadas: {comparacoes}")
    return -1


busca_sequencial(numeros, 95)
busca_binaria(numeros, 95)
