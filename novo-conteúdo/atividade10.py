def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"

assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável"
assert classificar_temperatura(25) == "Agradável"
assert classificar_temperatura(26) == "Quente"

# O teste de 15 é importante porque é o limite entre Frio e Agradável.