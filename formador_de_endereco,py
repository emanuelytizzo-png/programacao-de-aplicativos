def gerar_etiqueta(rua, numero, bairro, cidade, cep, urgencia=False):
    """
    Padroniza o endereço para impressão em etiquetas de envio.
    """
  
    endereco_formatado = f"RUA: {rua.upper()}, Nº: {numero} - BAIRRO: {bairro.upper()} - CIDADE: {cidade.upper()} - CEP: {cep}"
    
    if urgencia:
        endereco_formatado = "!!! URGENTE !!! " + endereco_formatado
        
    return endereco_formatado

etiqueta1 = gerar_etiqueta("Rua das Flores", "123", "Jardim Paulista", "São Paulo", "01000-000")
print(etiqueta1)

etiqueta2 = gerar_etiqueta("Av. Central", "SN", "Centro", "Rio de Janeiro", "20000-000", urgencia=True)