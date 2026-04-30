def somar_carrinho(lista_precos):
    """
    Soma os produtos e aplica 10% de desconto se o total > R$ 500.
    """
    total = sum(lista_precos)
    
    if total > 500:
        total = total * 0.90 
        print(f"Desconto de 10% aplicado!")
        
    return total

carrinho = [150.00, 230.50, 50.00, 100.00]

valor_final = somar_carrinho(carrinho)

print(f"Lista de produtos: {carrinho}")
print(f"O valor final a ser pago é: R$ {valor_final:.2f}")    