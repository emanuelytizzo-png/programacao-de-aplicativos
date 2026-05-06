def analisar_vendas (nome, lista_vendas, meta_mensal)
media = (lista_vendas) len (lista_vendas)

if media => meta_mensal:
    status = "bateu" 
else:
    status =  "não bateu"

return f"O vendedor {nome} teve média de {media:.2f} e {status} a meta."

vendedor = "carlos"
vendas_carlos = [1200, 1500, 1100, 1900]
meta = 1400
resultado = analisar_vendas(vendedor, vendas_carlos, meta)
print(resultado)  
