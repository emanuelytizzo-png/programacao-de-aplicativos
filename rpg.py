ataque_do_heroi = int(input("dano do heroi: "))
defesa_do_vilao = int(input("defesa do vilao: "))

dano = ataque_do_heroi - defesa_do_vilao

if ataque_do_heroi > defesa_do_vilao:
    print("Ataque critico. O dano causado foi: " , dano)
if defesa_do_vilao > ataque_do_heroi:
    print("ataque neutralizado. dano; " , dano)
    