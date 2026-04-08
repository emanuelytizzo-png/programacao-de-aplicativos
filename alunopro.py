for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

soma = 0
for n in notas:
    soma += n

media = soma / 4

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")