# Função escolhida: desconto
# Regra encontrada: o desconto deve ser calculado em porcentagem.

# Função original
def calcular_desconto(preco, percentual):
    return preco - percentual

# Testes criados
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# A função estava errada porque diminuía o percentual diretamente
# do preço.

# Função corrigida
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

# Testando novamente
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# Regra encontrada: o desconto precisa ser calculado usando a porcentagem.
