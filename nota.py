nota = float(input("coloque a sua nota: "))
presença = int (input("coloque sua presença: "))

if nota >= 70 and presença >= 75:
    print("voce foi aprovado!")

elif nota <= 70 and presença <= 75:
    print("voce foi reprovado. verifique sua nota ou presença")

elif nota <= 70 and presença >= 75: 
    print("voce foi reprovado.")

elif nota >= 70 and presença <= 75:
    print("voce foi reprovado")
    