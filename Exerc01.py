def calculoImposto (salario):
    "Calculo do Imposto"
    imposto = 0

    if salario <= 1903.98:
        imposto = 0

    elif(salario > 1903.98 and salario <= 2826.65):
        imposto = (salario * 0.075) - 142.80

    elif(salario > 2826.65 and salario <= 3751.05):
        imposto = (salario * 0.15) - 354.80

    elif(salario > 3751.05 and salario <= 4664.68):
        imposto = (salario * 0.225) - 636.13

    elif(salario > 4664.68):
        imposto = (salario * 0.275) - 869.36

    return imposto

salario = input("Informe o salario a ser calculado o imposto: ")
salario = float(salario)

imposto = calculoImposto(salario)

print("O imposto em cima do Salario R$ %.2f é R$ %.2f" % (salario, imposto))