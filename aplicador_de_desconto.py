def aplicar_promocao(lista_precos):
    """
    Recebe uma lista de preços e aplica 15% de desconto
    em itens acima de R$ 100,00.
    """
    nova_lista = []
    for preco in lista_precos:
        if preco > 100.00:
            preco_desconto = preco * 0.85
            nova_lista.append(round(preco_desconto, 2)) 
        else:
            nova_lista.append(preco)
    
    return nova_lista
compras = [150.0, 80.0, 200.0, 50.0]
compras_atualizadas = aplicar_promocao(compras)
print(f"Lista original: {compras}")
print(f"Lista com desconto: {compras_atualizadas}")