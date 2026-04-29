def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    """
    Verifica se o candidato está aprovado baseado em nota, 
    experiência e certificação.
    """
    
    if (nota_teste > 80 and anos_xp > 2) or possui_certificacao:
        return True
    else:
        return False

print("--- Sistema de Triagem de RH ---")

try:
    nota = float(input("Digite a nota técnica do candidato (0-100): "))
    xp = float(input("Digite os anos de experiência: "))
   
    cert = input("Possui certificação? (s/n): ").lower() == 's'

    aprovado = verificar_aprovacao(nota, xp, cert)

    if aprovado:
        print("Resultado: [CONTRATAR]")
    else:
        print("Resultado: [DESCARTAR]")

except ValueError:
    print("Erro: Por favor, insira números válidos para nota e experiência.")