def esta_na_lista(lista, nome_para_buscar):
    """
    Percorre uma lista para encontrar um nome específico.
    """
    for item in lista:
        if item == nome_para_buscar:
            return "Encontrado!"
    
    return "Não disponível"

minha_lista = ["maçã", "banana", "uva", "laranja", "melancia"]

busca1 = "banana"
resultado1 = esta_na_lista(minha_lista, busca1)
print(f"Busca por '{busca1}': {resultado1}")

busca2 = "pera"
resultado2 = esta_na_lista(minha_lista, busca2)
print(f"Busca por '{busca2}': {resultado2}")

lista_ferramentas = ["martelo", "chave inglesa", "prego"]
busca3 = "martelo"
print(f"Busca por '{busca3}' em ferramentas: {esta_na_lista(lista_ferramentas, busca3)}")