curso = input("voce concluiu o curso de programaçao?")

if curso == "sim": 
    instrutor = input ("o instrutor está na sala?")
    if instrutor == "sim":
        print ("Acesso liberado: operação iniciada")
else:
    print ("aguarde o instrutor para ligar a maquina")

else:
    print ("acesso negado: faça o treinamento primeiro")
    