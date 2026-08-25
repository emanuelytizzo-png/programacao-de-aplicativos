# Função original (não alterada)
def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"


# Bloco de Testes
try:
    # 1. Caso Comum: Média acima de 6
    assert (
        situacao_aluno(8.5) == "Aprovado"
    ), "Erro: 8.5 deveria retornar 'Aprovado'"

    # 2. Caso de Limite: Média exatamente igual a 6
    assert (
        situacao_aluno(6.0) == "Aprovado"
    ), "Erro: limite 6.0 deveria retornar 'Aprovado'"

    # 3. Caso de Limite: Média exatamente igual a 4
    assert (
        situacao_aluno(4.0) == "Recuperação"
    ), "Erro: limite 4.0 deveria retornar 'Recuperação'"

    # 4. Caso Comum: Média abaixo de 4
    assert (
        situacao_aluno(3.0) == "Reprovado"
    ), "Erro: 3.0 deveria retornar 'Reprovado'"

    # 5. Caso de Limite: Média com decimal (próxima à mudança de faixa)
    assert (
        situacao_aluno(5.9) == "Recuperação"
    ), "Erro: 5.9 deveria retornar 'Recuperação'"
    assert (
        situacao_aluno(3.9) == "Reprovado"
    ), "Erro: 3.9 deveria retornar 'Reprovado'"

    print("Todos os testes da situação do aluno passaram com sucesso!")

except AssertionError as e:
    print(f"Falha no teste: {e}")
