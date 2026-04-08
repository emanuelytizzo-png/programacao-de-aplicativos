salarios = [1500, 2500, 1800, 3200, 2000]

for salario in salarios:
    if salario <= 2000:
        imposto = salario * 0.10
    else:
        imposto = salario * 0.20
    print(f"Salário: R$ {salario:.2f} - Imposto: R$ {imposto:.2f}")