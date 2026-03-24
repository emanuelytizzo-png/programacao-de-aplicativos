vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]
try:
    indice = int(input("Digite o número da vaga (0 a 3): "))
 if 0 <= indice <= 3:
        if indice % 2 == 0 and vagas[indice] == "Livre":
            print(f"Vaga {indice} autorizada para estacionar.")
        else:
            print(f"Vaga {indice} não atende aos requisitos (deve ser par E livre).")
    else:
        print("Número de vaga inválido. Digite um número entre 0 e 3.")

except ValueError:
    print("Por favor, digite um número inteiro válido.")