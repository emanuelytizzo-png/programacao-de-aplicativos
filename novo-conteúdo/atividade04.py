def eh_par(numero):
    return numero % 2 == 0

assert eh_par(3) is False

# O erro estava no teste. A função está correta porque 3 é ímpar,
# então o resultado deve ser False.