def gerar_relatorio_saude (nome, peso, altura, idade):
if imc < 18.5:
        categoria = "Baixo peso"
elif 18.5 <= imc <= 24.9:
        categoria = "Normal"
elif 25 <= imc <= 29.9:
        categoria = "Sobrepeso"
else:
        categoria = "Obesidade"
relatorio = (f"Olá, {nome}. Com base nos dados informados (idade: {idade} anos), ")
             f"seu IMC é {imc:.2f}, o que se classifica como: {categoria}.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (kg), ex: 70.5: "))
altura = float(input("Digite sua altura (m), ex: 1.75: "))

