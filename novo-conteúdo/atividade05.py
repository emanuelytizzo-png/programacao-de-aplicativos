def frete_gratis(valor):
    return valor >= 200

assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True


def pode_votar(idade):
    return idade >= 16

assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True


def senha_valida(senha):
    return len(senha) >= 8

assert senha_valida("1234567") is False
assert senha_valida("12345678") is True
assert senha_valida("123456789") is True

