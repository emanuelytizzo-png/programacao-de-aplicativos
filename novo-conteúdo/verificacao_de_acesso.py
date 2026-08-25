# Função original (não alterada)
def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False


# Bloco de Testes
try:
    # 1. Caso Comum: Pessoa maior de idade desacompanhada
    assert (
        pode_entrar(25, False) is True
    ), "Erro: maior de idade desacompanhado deveria entrar"

    # 2. Caso Comum: Pessoa menor de idade acompanhada
    assert (
        pode_entrar(14, True) is True
    ), "Erro: menor de idade acompanhado deveria entrar"

    # 3. Caso Comum: Pessoa menor de idade desacompanhada
    assert (
        pode_entrar(15, False) is False
    ), "Erro: menor de idade desacompanhado não deveria entrar"

    # 4. Caso de Limite: Pessoa com exatamente 18 anos (fronteira da maioridade)
    assert (
        pode_entrar(18, False) is True
    ), "Erro: pessoa com exatamente 18 anos desacompanhada deveria entrar"

    # 5. Caso de Limite: Pessoa com 17 anos acompanhada (fronteira da menoridade)
    assert (
        pode_entrar(17, True) is True
    ), "Erro: pessoa com 17 anos acompanhada deveria entrar"

    print("Todos os testes de verificação de acesso passaram com sucesso!")

except AssertionError as e:
    print(f"Falha no teste: {e}")
