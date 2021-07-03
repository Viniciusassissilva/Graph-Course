import Extra9
import Extra10
import os

def exerc11():
    "Exercicio 1 - 01 - calculo de area e perimetro"
    raio = float(input("Informe o raio: "))

    area = 3.14 * raio * raio
    perimetro = 2 * 3.14 * raio

    print("A area é %f e o perimetro é %f" % (area, perimetro))

    os.system("pause")
    return subMenu1()

def exerc12():
    "Exercicio 1 - 02 - conversão de Fahrenheit para Celsius"
    temperatura = float(input("Informe a temperatura em Fahrenheit: "))

    celcius = (5 * ((temperatura - 32)/9))

    print("%.2f Fahrenheit convertendo para Celcius é %.2f C°" % (temperatura, celcius))

    os.system("pause")
    return subMenu1()

def exerc13():
    "Exercicios 1 - 03 - conversão real para dolar"

    real = float(input("Informe o valor em reais, R$: "))

    dolar = real/5.32

    print("R$ %.2f é US$ %.2f" % (real, dolar))

    os.system("pause")
    return subMenu1()

def exerc14():
    "Exercicio 1- 04 - Calculo do salario"

    valorHora = float(input("Insira o valor de quanto ganha por hora, R$: "))
    diasMes = int(input("Insira quantos horas no mês trabalha: "))

    salarioBruto = valorHora * diasMes
    impostoRenda = salarioBruto * 0.15
    inss = salarioBruto * 0.1
    sindicato = salarioBruto * 0.02

    salarioLiquido = salarioBruto - (inss + impostoRenda + sindicato)

    print("Salario bruto R$ %.2f \n"
          "Imposto de renda R$ %.2f \n"
          "INSS R$ %.2f \n"
          "Sindicato R$ %.2f \n"
          "Salario Liquido R$ %.2f" % (salarioBruto, impostoRenda, inss, sindicato, salarioLiquido))

    os.system("pause")
    return subMenu1()

def exerc15():
    "Exercicios 1 - 05 - Loja de Tintas"

    area = int(input("Informe o tamanho de area a ser pintada: "))

    min = 3 * 18

    compra = area / min

    if(compra <= 1):
        print("O espaço é muito pequeno")
        print("Sera necessario 1 lata de tinta (para pintar tudo) - Valor R$ 80,00")
    else:
        compra1 = float(area % min)
        compra2 = int(area / min)

        if(compra1 == 0):

            valor = 80 * compra2
            print("Sera necessario %d lata(s) de tinta - O valor sera R$ %d" % (compra2, valor))

        if(compra1 > 0):

            valor = 80 * (compra2)
            print("Sera necessario %d lata(s) de tinta - O valor sera R$ %d (faltara cobrir %d m²)" % (compra2, valor, compra1))
            compra2 = compra2 + 1
            valor = 80 * (compra2)
            print("Sera necessario %d lata(s) de tinta - O valor sera R$ %d (para pintar tudo)" % (compra2, valor))

    os.system("pause")
    return subMenu1()

def exerc16():
    "Exercicio 1 - 06 - Calculo de Download"

    tamanho = float(input("Informe o tamanho do arquivo para download(MB): "))
    velocidade = int(input("Informe a velocidade da internet(Mbps): "))

    tempo = (tamanho / velocidade) / 60

    print("O tempo para download: %.2f minutos" % (tempo))

    os.system("pause")
    return subMenu1()
def exerc21():
    "Exercicio 2 - 01 - Calculo do IMC"

    peso = float(input("Insira seu peso em Kg: "))
    altura = float(input(("Insira sua altura em metros: ")))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 25:
        print("Peso normal")
    else:
        print("Sobrepeso")

    os.system("pause")
    return subMenu2()

def exerc22():
    "Exercicio 2 - 02 - Calculo imposto de renda"
    imposto = 0

    salario = input("Informe o salario a ser calculado o imposto: ")
    salario = float(salario)

    if salario <= 1903.98:
        imposto = 0

    elif (salario > 1903.98 and salario <= 2826.65):
        imposto = (salario * 0.075) - 142.80

    elif (salario > 2826.65 and salario <= 3751.05):
        imposto = (salario * 0.15) - 354.80

    elif (salario > 3751.05 and salario <= 4664.68):
        imposto = (salario * 0.225) - 636.13

    elif (salario > 4664.68):
        imposto = (salario * 0.275) - 869.36

    print("O imposto em cima do Salario R$ %.2f é R$ %.2f" % (salario, imposto))

    os.system("pause")
    return subMenu2()
def exerc23():
    "Exercicio 2 - 03 - Posto de combustivel"

    print(" Desconto: \n"
          "Alcool até 20 L: 3% por litro \n"
          "Alcool acima de 20 L: 5% por litro \n"
          "Gasolina até 20 L: 4% por Litro \n"
          "Gasolina acima de 20L: 5% por litro")
    while True:
        tipo = input("Insira o tipo de combustivel que deseja abastecer:\n"
                     "Alcool - A\n"
                     "Gasolina - G\n"
                     "Insira: ")
        if tipo == "A" or tipo == "a":
            litros = float(input("Insira a quantidade de combustivel: "))
            if litros <= 20:
                desconto = (litros * 2.80) * 0.03
                valor1 = litros * 2.80
                valor2 = valor1 - desconto
                print("A valor do combustivel foi R$ %.2f \n"
                      "O desconto foi de %.2f \n"
                      "O valor a se pagar é R$ %.2f" % (valor1, desconto, valor2))
            elif litros > 20:
                desconto = (litros * 2.80) * 0.05
                valor1 = litros * 2.80
                valor2 = valor1 - desconto
                print("A valor do combustivel foi R$ %.2f \n"
                      "O desconto foi de %.2f \n"
                      "O valor a se pagar é R$ %.2f" % (valor1, desconto, valor2))
            break
        elif tipo == "G" or tipo == "g":
            litros = float(input("Insira a quantidade de combustivel: "))
            if litros <= 20:
                desconto = (litros * 4.20) * 0.04
                valor1 = litros * 4.20
                valor2 = valor1 - desconto
                print("A valor do combustivel foi R$ %.2f \n"
                      "O desconto foi de %.2f \n"
                      "O valor a se pagar é R$ %.2f" % (valor1, desconto, valor2))
            elif litros > 20:
                desconto = (litros * 4.20) * 0.06
                valor1 = litros * 4.20
                valor2 = valor1 - desconto
                print("A valor do combustivel foi R$ %.2f \n"
                      "O desconto foi de %.2f \n"
                      "O valor a se pagar é R$ %.2f" % (valor1, desconto, valor2))
            break

    os.system("pause")
    return subMenu2()

def exerc24():
    "Exercicio 2 - 04 - Caixa Eletronico"
    while True:
        valor = int(input("Insira o valor do saque (multiplo de 10)\n"
                          "Valor maximo R$ 1000.00\n"
                          "Valor minimo R$ 10.00\n"
                          "Insira: "))
        multiplo10 = valor % 10

        if multiplo10 == 0 and valor <= 1000:
            if valor >= 10 and valor < 50:
                notas10 = valor / 10
                print("%d nota(s) de R$ 10.00" % (notas10))

            elif valor >= 50 and valor < 100:
                notas50 = valor / 50
                notas10 = (valor % 50) / 10
                print("%d nota(s) de R$ 10.00 \n"
                      "%d nota(s) de R$ 50.00 "% (notas10, notas50))

            elif valor >= 100 and valor < 200:
                notas100 = valor / 100
                notas50 = (valor % 100) / 50
                notas10 = ((valor % 100) % 50) / 10
                print("%d nota(s) de R$ 10.00 \n"
                      "%d nota(s) de R$ 50.00 \n"
                      "%d nota(s) de R$ 100.00" % (notas10, notas50, notas100))
            elif valor >= 200:
                notas200 = valor / 200
                notas100 = (valor % 200) / 100
                notas50 = ((valor % 200) % 100) / 50
                notas10 = ((((valor % 200) % 100) % 100) % 50) / 10
                print("%d nota(s) de R$ 10.00 \n"
                      "%d nota(s) de R$ 50.00 \n"
                      "%d nota(s) de R$ 100.00 \n"
                      "%d nota(s) de R$ 200.00" % (notas10, notas50, notas100, notas200))
            break
        elif multiplo10 != 0 and (valor > 1000 or valor < 10) :
            print(("Insira um valor entre R$ 10 e R$ 1000.00 "))
        else:
            print("Insira um multiplo de 10, exemplo: R$ 200.00")

    os.system("pause")
    return subMenu2()

def exerc31():
    "Exercicio 3 - 01 - Validar dados"

    while True:
        nome = input("Insira seu nome (min. 3 caracterios): ")
        idade = int(input("Insira sua idade(entre 0 a 150): "))
        salario = float(input("Insira seu salario(maior que zero): "))
        sexo = input("Insira seu sexo(F - feminino / M - masculino): ")
        estadoCivil = input(("Estado civil: \n"
                             "Solteiro - S\n"
                             "Casado - C\n"
                             "Viuva - V\n"
                             "Divorciado - D\n"
                             "Insira: "))
        tamanhoNome =len(nome)

        if tamanhoNome < 3:
            print("Nome muito pequeno")
        elif idade < 0 and idade > 150:
            print("Idade incorreta")
        elif salario <= 0:
            print("insira um salario maior que zero")
        elif sexo != "F" and (sexo != "f" and (sexo != "m" and sexo != "M")):
            print("Insira um sexo correto, exemplo : F")
        elif estadoCivil != "S" and estadoCivil != "C" and estadoCivil != "V" and estadoCivil != "D":
            print("Insira um estado civil correto, exemplo : C")
        else:
            print("Nome: %s \n"
                  "Idade: %d \n"
                  "Salario: %.2f \n"
                  "Sexo: %s \n"
                  "Estado Civil: %s" % (nome, idade, salario, sexo, estadoCivil))
            break

    os.system("pause")
    return subMenu3()

def exerc32():
    "Exercicio 3 - 02 - Achar o maior numero"
    vet = []

    for _ in range(5):
        vet.append(int(input("Digite um número: ")))

    maximo = max(vet)

    for num in range(len(vet)):
        print("%d" % (vet[num]), end=" ")

    print()
    print("Na lista o maior numero é: %d" % (maximo))

    os.system("pause")
    return subMenu3()

def exerc33():
    "Exercicio 3 - 03 - Soma e media"

    vet = []

    for _ in range(5):
        vet.append(int(input("Digite um número: ")))

    soma = sum(vet)
    media = float(sum(vet)/len(vet)) # nao achei a função AVG

    print("A soma dos numeros é: %d\n"
          "A media dos numeros é: %.2f" % (soma, media))

    os.system("pause")
    return subMenu3()

def exerc34():
    "Exercicio 3 - 04 - Pares e Impares"

    vet = []
    pares = []
    impares = []

    for _ in range(10):
        vet.append(int(input("Digite um número: ")))

    for num in range(len(vet)):
        if vet[num] % 2 == 0:
            pares.append(vet[num])
        else:
            impares.append((vet[num]))

    print(pares)
    print(impares)

    qntpar = len(pares)
    qntimpar = len(impares)

    print("Quantidade de pares: %d\n"
          "Quantidade de impares: %d" % (qntpar, qntimpar))

    os.system("pause")
    return subMenu3()

def exerc35():
    "Exercicio 3 - 05 - Numero primo"

    numero = int(input("Insira o numero: "))
    cont = 0
    i = 2

    while i <= numero:
        if numero % i == 0:
            cont += 1
        i += 1

    if cont == 1:
        print("%d é primo" % (numero))

    else:
        print("%d não é primo" % (numero))

    os.system("pause")
    return subMenu3()

def exerc36():
    "Exercicio 3 - 06 - Quais numeros dividem"

    numero = int(input("Insira o numero: "))
    divisores = []
    cont = 0
    i = 2

    while i <= numero:
        if numero % i == 0:
            divisores.append(i)
            cont += 1
        i += 1

    if cont == 1:
        print("%d é primo" % (numero))

    else:
        print("O divisores de %d são" % (numero) + str(divisores))

    os.system("pause")
    return subMenu3()

def exerc37():
    "Exercicio 3 - 07 - Quadrado de asterico"
    n = int(input("Insira o tamanho da matriz: "))

    quadrado = [[" " for _ in range(n)] for _ in range(n)]

    for x in range(len(quadrado)):
        for j in range(len(quadrado)):
            if (j == 0) or (j == len(quadrado) - 1) or (x == 0) or (x == len(quadrado) - 1):
                quadrado[x][j] = "*"

    for x in range(len(quadrado)):
        print("")
        for j in range(len((quadrado))):
            print(quadrado[x][j], end=" ")
    print()

    os.system("pause")
    return subMenu3()

def exerc38():
    "Exercico 3 - 08 - Triangulo de asterico"
    n = int(input("Insira o tamanho da matriz: "))

    quadrado = [[" " for _ in range(n)] for _ in range(n)]

    for x in range(len(quadrado)):
        for j in range(len(quadrado)):
            if j <= x:
                quadrado[x][j] = "*"

    for x in range(len(quadrado)):
        print("")
        for j in range(len((quadrado))):
            print(quadrado[x][j], end=" ")

    print()
    os.system("pause")
    return subMenu3()

def exerc39():
    "Exercicio 3 - 09 - Armazenamento de notas"

    conceitoA = []
    conceitoB = []
    conceitoC = []
    conceitoD = []
    conceitoE = []
    while True:
        nota = float(input("Insira a nota: "))

        if nota >= 9 and nota <= 10:
            conceitoA.append(nota)
        elif nota >= 8 and nota < 9:
            conceitoB.append(nota)
        elif nota >= 7 and nota < 8:
            conceitoC.append(nota)
        elif nota >= 6 and nota < 7:
            conceitoD.append(nota)
        elif nota >= 0 and nota < 6:
            conceitoE.append(nota)
        elif nota == -1:
            break
        else:
            print("Digite um nota valida ou -1 para sair")

    print("Conceito A" + str(conceitoA))
    print("Conceito B" + str(conceitoB))
    print("Conceito C" + str(conceitoC))
    print("Conceito D" + str(conceitoD))
    print("Conceito E" + str(conceitoE))

    os.system("pause")
    return subMenu3()

def potencia(num, pot):

    i = 1
    resultado = 1

    while i <= pot:
        resultado = resultado * num
        i += 1
    return resultado

def exerc41():
    "Exercicio 4 - 01 - Calculo da potencia"
    numero = int(input("Insira o numero: "))
    pot = int(input("Insira a potencia: "))

    resultado = potencia(numero, pot)
    print("O numero %d^%d = %d" % (numero, pot, resultado))

    os.system("pause")
    return subMenu4()

def positivos(vet):

    positivo = []

    for i in range(len(vet)):
        if vet[i] >= 0 :
            positivo.append(vet[i])

    return positivo

def exerc42():
    "Exercicio 4 - 02 - Verificação de numero inteiro"
    inteiro = []

    while True:
        inteiro.append(int(input("Insira um numero inteiro: ")))
        codigo = input("Deseja continuar S/N: ")
        if codigo == "N" or codigo == "n":
            break

    positivo = positivos(inteiro)
    print("Os numeros positivos são: " + str(positivo))

    os.system("pause")
    return subMenu4()

def inverteString(string):

    inverso = ""
    tamanho = len(string)
    i = tamanho - 1
    while i >= 0:
        inverso = inverso + string[i]
        i -= 1

    return inverso

def exerc43():
    "Exercicio 4 - 03 - Inverter a palavra"

    palavra = str(input("Insira a palavra: "))
    inverso = inverteString(palavra)
    print("O inverso da palavra %s é %s" % (palavra, inverso))

    os.system("pause")
    return subMenu4()

def palindromo(string):

    tamanho = len(string)
    i = tamanho - 1
    inverso = ""

    while i >= 0:
        inverso = inverso + string[i]
        i -= 1

    if inverso == string:
        return True
    else:
        return False

def exerc44():
    "Exercicio 4 - 04 - Palindromo"

    palavra = str(input("Insira a palavra: "))


    if palindromo(palavra):
        print("%s é um palíndromo" % (palavra))
    else:
        print("%s não é um palíndromo" % (palavra))

    os.system("pause")
    return subMenu4()

def recorrenciaChar(string, char):
    contador = 0

    for i in range(len(string)):
        if char == string[i]:
            contador += 1

    return contador

def exerc45():
    "Exercicio 4 - 06 - Encontrando caracteres na String"

    string = str(input("Insira a string: "))
    char = str(input("Insira o caractere que deseja saber a recorrencia: "))

    contador = recorrenciaChar(string, char)

    print("Na String:\n"
          "%s\n"
          "O caractere '%s' se repete %d vezes" % (str(string), str(char), contador))

    os.system("pause")
    return subMenu4()

def passarSegundos(dias, horas, minutos, segundos):

    segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + (segundos)

    return segundos
def exerc46():
    "Exercicio 4 - 6 - Calcular o tempo em segundos"

    dias = int(input("Insira quantos dias: "))
    horas = int(input("Insira quantas horas : "))
    minutos = int(input("Insira quantos minutos: "))
    segundos = int(input("Insira quantos segundos: "))

    totalsegundos = passarSegundos(dias, horas, minutos, segundos)

    print("%d dia(s) : %d hora(s) : %d minuto(s) : %d segundo(s) em segundos é %d segundos" % (dias, horas, minutos, segundos, totalsegundos))

    os.system("pause")
    return subMenu4()

def contarVogal(string):
    vogais = 0

    for i in range(len(string)):
        if "a" == string[i]:
            vogais += 1
        elif "e" == string[i]:
            vogais += 1
        elif "i" == string[i]:
            vogais += 1
        elif "o" == string[i]:
            vogais += 1
        elif "u" == string[i]:
            vogais += 1

    return vogais

def exerc47():
    "Exercicio 4 - 7 - Contar vogais"

    palavra = str(input("Insira a string: "))

    print("Na string: \n"
          "%s\n"
          "Tem %d vogais" % (palavra, contarVogal(palavra)))

    os.system("pause")
    return subMenu4()

def mdc(num1, num2):

    div1 = []
    div2 = []
    divComum = []

    i = 1
    j = 1

    while i <= num1:
        if num1 % i == 0:
            div1.append(i)
        i += 1

    while j <= num2:
        if num2 % j == 0:
            div2.append(j)
        j += 1

    for x in range(len(div1)):
        for y in range(len(div2)):
            if div1[x] == div2[y]:
                divComum.append(div1[x])

    maxdiv = max(divComum)

    return maxdiv

def exerc48():
    "Exercico 4 - 8 - Calcular o MDC"

    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))

    print("O MDC entre %d e %d é %d" % (num1, num2, mdc(num1, num2)))

    os.system("pause")
    return subMenu4()

def exerc49():
    "Exercicio 4 - 9 - Criar uma classe funcionario"

    funcionario = []

    while True:
        nome = str(input("Nome do Funcionario: "))
        salario = float(input("Salario do Funcionario: R$ "))
        funcionario.append(Extra9.Funcionario(nome, salario))

        codigo = str(input("Você quer continuar S/N: "))
        if codigo == "N" or codigo == "n":
            break

    for i in range(len(funcionario)):
        print("Nome: " + funcionario[i].nome, "R$: " + funcionario[i].salario)

    os.system("pause")
    return subMenu4()

def exerc410():
    "Exercicio 4 - 10 - Criar a Classe carro"

    consumoCarro = int(input("Insira o consumo do carro (Km/L): "))
    qntCombustivel = float(input(("Insira a quantidade de Combustivel (Litros): ")))
    carro1 = Extra10.Carro(consumoCarro, qntCombustivel)


    carro1.andar(100)
    carro1.abastecer(100)
    carro1.andar(30)

    os.system("pause")
    return subMenu4()

def funcaoMenu():
    "função do menu"
    print("1 - Entrada e Saida, Variaveis e Operadores \n"
          "2 - Comandos Condicionais \n"
          "3 - Comandos de Repetição \n"
          "4 - Funções e Orientação a Objetos \n"
          "0 - Sair")

    menuPrincipal = int(input("Seleciona a opção: "))

    if menuPrincipal == 1:
        subMenu1()
    elif menuPrincipal == 2:
        subMenu2()
    elif menuPrincipal == 3:
        subMenu3()
    elif menuPrincipal == 4:
        subMenu4()
    elif menuPrincipal == 0:
        print("Finalizando Exercicios.")
        quit()

    else: return funcaoMenu()

def subMenu1():
    "Função de submenu"
    print("Exercicio 01 - 1 \n"
          "Exercicio 02 - 2 \n"
          "Exercicio 03 - 3 \n"
          "Exercicio 04 - 4 \n"
          "Exercicio 05 - 5 \n"
          "Exercicio 06 - 6 \n"
          "Menu Anterior - 0")

    opcao = int(input("Seleciona a opção: "))

    if opcao == 1:
        exerc11()
    elif opcao == 2:
        exerc12()
    elif opcao == 3:
        exerc13()
    elif opcao == 4:
        exerc14()
    elif opcao == 5:
        exerc15()
    elif opcao == 6:
        exerc16()
    elif opcao == 0:
        return funcaoMenu()
    else:
        print("Escolha uma opção correta")
        return subMenu1()

def subMenu2():
    "Função de submenu"
    print("Exercicio 01 - 1 \n"
          "Exercicio 02 - 2 \n"
          "Exercicio 03 - 3 \n"
          "Exercicio 04 - 4 \n"
          "Sair - 0")

    opcao = int(input("Seleciona a opção: "))

    if opcao == 1:
        exerc21()
    elif opcao == 2:
        exerc22()
    elif opcao == 3:
        exerc23()
    elif opcao == 4:
        exerc24()
    elif opcao == 0:
        return funcaoMenu()
    else:
        print("Escolha uma opção correta")
        return subMenu2()

def subMenu3():
    "Função de submenu"
    print("Exercicio 01 - 1 \n"
          "Exercicio 02 - 2 \n"
          "Exercicio 03 - 3 \n"
          "Exercicio 04 - 4 \n"
          "Exercicio 05 - 5 \n"
          "Exercicio 06 - 6 \n"
          "Exercicio 07 - 7 \n"
          "Exercicio 08 - 8 \n"
          "Exercicio 09 - 9 \n"
          "Sair - 0")

    opcao = int(input("Seleciona a opção: "))

    if opcao == 1:
        exerc31()
    elif opcao == 2:
        exerc32()
    elif opcao == 3:
        exerc33()
    elif opcao == 4:
        exerc34()
    elif opcao == 5:
        exerc35()
    elif opcao == 6:
        exerc36()
    elif opcao == 7:
        exerc37()
    elif opcao == 8:
        exerc38()
    elif opcao == 9:
        exerc39()
    elif opcao == 0:
        return funcaoMenu()
    else:
        print("Escolha uma opção correta")
        return subMenu3()

def subMenu4():
    "Função de submenu"
    print("Exercicio 01 - 1 \n"
          "Exercicio 02 - 2 \n"
          "Exercicio 03 - 3 \n"
          "Exercicio 04 - 4 \n"
          "Exercicio 05 - 5 \n"
          "Exercicio 06 - 6 \n"
          "Exercicio 07 - 7 \n"
          "Exercicio 08 - 8 \n"
          "Exercicio 09 - 9 \n"
          "Exercicio 10 - 10 \n"
          "Sair - 0")

    opcao = int(input("Seleciona a opção: "))

    if opcao == 1:
        exerc41()
    elif opcao == 2:
        exerc42()
    elif opcao == 3:
        exerc43()
    elif opcao == 4:
        exerc44()
    elif opcao == 5:
        exerc45()
    elif opcao == 6:
        exerc46()
    elif opcao == 7:
        exerc47()
    elif opcao == 8:
        exerc48()
    elif opcao == 9:
        exerc49()
    elif opcao == 10:
        exerc410()
    elif opcao == 0:
        return funcaoMenu()
    else:
        print("Escolha uma opção correta")
        return subMenu4()

"MAIN"
funcaoMenu()
