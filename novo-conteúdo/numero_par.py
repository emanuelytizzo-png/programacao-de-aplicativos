def eh_par(numero):
    return numero % 2 == 0

# Bloco de Testes
try:
    # 1. Caso Comum: Número par positivo
    assert eh_par(4) is True, "Erro: 4 deveria ser considerado par"

    # 2. Caso Comum: Número ímpar positivo
    assert eh_par(7) is False, "Erro: 7 não deveria ser considerado par"

    # 3. Caso de Limite: Zero
    assert eh_par(0) is True, "Erro: 0 deveria ser considerado par"

    # 4. Caso de Limite: Número negativo (par e ímpar)
    assert eh_par(-2) is True, "Erro: -2 deveria ser considerado par"
    assert eh_par(-3) is False, "Erro: -3 não deveria ser considerado par"

    print("Todos os testes passaram com sucesso!")

except AssertionError as e:
    print(f"Falha no teste: {e}")