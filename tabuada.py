numero = int(input("Digite um número: "))

lista = list(range(1, 11))

for i in lista:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")