def calcular_area(largura, comprimento):
    """Calcula a área multiplicando largura por comprimento."""
    area = largura * comprimento
    return area

print("--- Calculadora de Área de Terrenos (3 terrenos) ---\n")

contador = 0

while contador < 3:
    print(f"Terreno {contador + 1}:")
    
    l = float(input("Digite a largura (m): "))
    c = float(input("Digite o comprimento (m): "))
    
    area_terreno = calcular_area(l, c)
    print(f"A área do terreno é: {area_terreno:.2f} m²\n")
 
    contador += 1

print("Cálculos finalizados.")