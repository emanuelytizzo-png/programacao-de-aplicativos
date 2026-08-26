def buscar_nome(lista, nome):
    return nome in lista

assert buscar_nome(["Ana", "João"], "Ana") is True
assert buscar_nome([], "Ana") is False
assert buscar_nome(["Ana"], "João") is False


def tem_senha_valida(senha):
    return len(senha) >= 8

assert tem_senha_valida("1234567") is False
assert tem_senha_valida("12345678") is True
assert tem_senha_valida("123456789") is True

# Ao buscar um nome em uma lista vazia, o resultado é False,
# porque não existe nenhum nome na lista.