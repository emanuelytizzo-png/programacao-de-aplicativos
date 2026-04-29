def converter_km_para_ms(velocidade_kmh):
    """
    Converte velocidade de km/h para m/s dividindo por 3.6.
    """
    velocidade_ms = velocidade_kmh / 3.6
    return velocidade_ms

try:
    velocidade_usuario = float(input("Digite a velocidade em km/h: "))

    if velocidade_usuario > 80:
        resultado_ms = converter_km_para_ms(velocidade_usuario)
        
        print(f"Velocidade: {velocidade_usuario} km/h equivale a {resultado_ms:.2f} m/s.")
        print("Aviso: Reduza a velocidade!")
    else:
        print("Velocidade dentro do limite ou segura.")

except ValueError:
    print("Por favor, digite um número válido para a velocidade.")