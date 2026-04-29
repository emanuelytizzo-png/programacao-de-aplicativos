def eh_par(numero):
    """
    Retorna True se o número for par e False se for ímpar.
    Usa o operador % para verificar o resto da divisão por 2.
    """
    if numero % 2 == 0:
        return True
    else:
        return False

try:
    entrada = int(input("Digite um número: "))
   
    if eh_par(entrada):
        print("Este número é par")
    else:
        print("Este número é ímpar")
        
except ValueError:
    print("Por favor, digite um número inteiro válido.")