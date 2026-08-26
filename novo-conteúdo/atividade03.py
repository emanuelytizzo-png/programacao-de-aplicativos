def calcular_desconto(preco, percentual):
    return preco - percentual

# Esses testes mostram que a função está errada.
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# O erro é que a função está diminuindo o percentual diretamente
# do preço. O correto é calcular a porcentagem.

def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45