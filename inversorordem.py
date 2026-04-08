numeros = []

for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Números na ordem inversa:")

while numeros:
    print(numeros.pop())