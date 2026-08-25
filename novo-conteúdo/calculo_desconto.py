# Função original (não alterada)
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


# Bloco de Testes
try:
    # 1. Caso de Limite: Produto sem desconto (0%)
    assert (
        calcular_desconto(100.0, 0) == 100.0
    ), "Erro: 0% de desconto em 100 deveria retornar 100.0"

    # 2. Caso Comum: Produto com 10% de desconto
    assert (
        calcular_desconto(200.0, 10) == 180.0
    ), "Erro: 10% de desconto em 200 deveria retornar 180.0"

    # 3. Caso Comum: Produto com 50% de desconto (metade do preço)
    assert (
        calcular_desconto(50.0, 50) == 25.0
    ), "Erro: 50% de desconto em 50 deveria retornar 25.0"

    # 4. Caso de Limite: Produto com 100% de desconto (grátis)
    assert (
        calcular_desconto(150.0, 100) == 0.0
    ), "Erro: 100% de desconto deveria retornar 0.0"

    # 5. Caso Comum: Produto com preço decimal
    assert (
        calcular_desconto(99.90, 10) == 89.91
    ), "Erro: 10% de desconto em 99.90 deveria retornar 89.91"

    print("Todos os testes de cálculo de desconto passaram com sucesso!")

except AssertionError as e:
    print(f"Falha no teste: {e}")
