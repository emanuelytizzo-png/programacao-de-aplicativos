def dobrar(numero):
    return numero * 2

# P
assert dobrar(3) == 6

# F
assert dobrar(0) == 1

# P
assert dobrar(-2) == -4

# Registro:
# O assert que falhou foi o segundo.
# O resultado real foi 0.
# A expectativa estava errada porque 0 vezes 2 é igual a 0, e não 1.