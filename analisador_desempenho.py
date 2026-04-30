def analisar_vendas(nome, lista_vendas, meta_mensal):
    total_vendas = sum(lista_vendas)
    quantidade_vendas = len(lista_vendas)
    media = total_vendas / quantidade_vendas
    if media >= meta_mensal:
        status = "bateu"
    else:
        status = "não bateu"
    return f"O vendedor {nome} teve média de {media:.2f} e {status} a meta."

nome_vendedor = "Carlos"
vendas_carlos = [1200, 1500, 1100, 1900]
meta = 1400

resultado = analisar_vendas(nome_vendedor, vendas_carlos, meta)
print(resultado)