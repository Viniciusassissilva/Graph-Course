def pesquisa(lista, item):

    "Retorna a posição no vetor, considerando que ele começa na posição 1"
    for num in range(len(lista)):
        if item == lista[num]:
            return num + 1

    return -1

codigo = 1
lista = []

while(codigo != 0):
    numero = int(input("Insira o numero: "))
    lista.append(numero)
    codigo = int(input(("Se deseja parar digite 0, caso contrario 1: ")))

item = int(input("Pesquise esse numero: "))

indice = pesquisa(lista, item)
print("O numero %d está na posição %d" % (item, indice))