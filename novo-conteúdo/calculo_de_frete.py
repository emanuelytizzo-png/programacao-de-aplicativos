# Função original (não alterada)
def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20


# Bloco de Testes
try:
    # 1. Caso Comum: Compra abaixo de R$ 100
    assert (
        calcular_frete(50.0) == 20
    ), "Erro: Compra abaixo de R$ 100 deveria cobrar R$ 20 de frete"

    # 2. Caso de Limite: Compra exatamente de R$ 100
    assert (
        calcular_frete(100.0) == 10
    ), "Erro: Compra de exatamente R$ 100 deveria cobrar R$ 10 de frete"

    # 3. Caso Comum: Compra entre R$ 100 e R$ 199,99
    assert (
        calcular_frete(150.50) == 10
    ), "Erro: Compra de R$ 150.50 deveria cobrar R$ 10 de frete"
    assert (
        calcular_frete(199.99) == 10
    ), "Erro: Compra de R$ 199.99 deveria cobrar R$ 10 de frete"

    # 4. Caso de Limite: Compra exatamente de R$ 200
    assert (
        calcular_frete(200.0) == 0
    ), "Erro: Compra de exatamente R$ 200 deveria ter frete grátis (0)"

    # 5. Caso Comum: Compra acima de R$ 200
    assert (
        calcular_frete(250.0) == 0
    ), "Erro: Compra acima de R$ 200 deveria ter frete grátis (0)"

    print("Todos os testes de cálculo de frete passaram com sucesso!")

except AssertionError as e:
    print(f"Falha no teste: {e}")
