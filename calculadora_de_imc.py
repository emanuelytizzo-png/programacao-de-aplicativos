def gerar_relatorio_saude(nome, peso, altura, idade):
    """
    Calcula o IMC, determina a classificação e retorna um relatório personalizado.
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Baixo peso"
    elif 18.5 <= imc < 25:
        categoria = "Normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    relatorio = (f"Olá, {nome}! Com {idade} anos e baseando-se nos dados informados "
                 f"(Peso: {peso}kg, Altura: {altura}m), seu IMC é {imc:.2f}. "
                 f"Classificação: {categoria}.")
    return relatorio

if __name__ == "__main__":
    print("--- Calculadora de IMC com Relatório Completo ---")

    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso (kg), ex: 70.5: "))
    altura = float(input("Digite sua altura (m), ex: 1.75: "))
    idade = int(input("Digite sua idade: "))
    
    resultado = gerar_relatorio_saude(nome, peso, altura, idade)
    print("\n--- Relatório de Saúde ---")
    print(resultado)