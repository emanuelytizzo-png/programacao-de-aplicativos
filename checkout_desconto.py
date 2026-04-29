def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    """
    Calcula o preço final com imposto e desconto.
    Regra: O preço final não pode ser negativo.
    """
    valor_com_imposto = valor_base * (1 + (imposto_percentual / 100))
    total = valor_com_imposto - cupom_desconto
    if total < 0:
        return 0.0
    
    return total
try:
    print("--- Sistema de Checkout ---")
    preco_prod = float(input("Digite o valor base do produto: R$ "))
    imposto = float(input("Digite a porcentagem do imposto estadual (ex: 10 para 10%): "))
    desconto = float(input("Digite o valor do cupom de desconto: R$ "))
    
    resultado = calcular_preco_final(preco_prod, imposto, desconto)
    
    print("-" * 30)
    print(f"Preço com imposto: R$ {preco_prod * (1 + (imposto/100)):.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Preço Final: R$ {resultado:.2f}")
    print("-" * 30)

except ValueError:
    print("Por favor, digite valores numéricos válidos.")