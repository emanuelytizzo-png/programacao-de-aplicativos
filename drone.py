print("- Fase de Indentificação - ") 
codigo = int(input("digite o codigo do drone"))
autorização = input ("O drone possui autorização de torre (s/n): ")

if codigo ==999 or autorização == "s":
    print("tudo certo: Iremos avançar para analise de pouso. ")
else: 
    print("ERRO 01: Drone não indentificado, retornando a base") 

print("- fase de analise de voo -")
bateria = float(input("digite o nivel de bateria do drone: "))
clima = input("qual o clima no momento: ") 
velocidade_do_vennto = float (input("digite a velocidade do vento (K/m): "))

if bateria < 10: 
    print("EMERGENCIA: pouse imediatamente!")
elif bateria >=10 and clima == "ensolarado" and (velocidade_do_vennto 30 or  clima chuvosd velocidade_do_vento < 18: 
    print("POUSO ALTORIZADO: iniciando decida") 
else:
    print("POUSO NEGADO: condições meterelogicas perigosas. Aguarde em orbita: ")