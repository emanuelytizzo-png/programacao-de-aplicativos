temperatura = float (input("qual a temperatura atual?: "))

if temperatura >= 80:
    print("perigo! Super aquecimento. ")
if temperatura >= 50:
    print("ventoinhas ligadas ao maximo. ")
elif temperatura < 50:
    print("temperatura estavel. ")
    