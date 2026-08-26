def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


assert situacao_aluno(8) == "Aprovado"

assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# 6 e 5.9 são casos de limite porque estão próximos da média mínima
# para aprovação. A média 6 é exatamente o limite para ser aprovado,
# enquanto 5.9 está logo abaixo desse limite.

# Teste extra
assert situacao_aluno(5) == "Reprovado"