def complementar(lista):

    A2 = []
    elementos = [i for i in range(len(lista))]

    for x in range(len(lista)):
        aux = []
        aux.append(x)
        A2.append(list((set(elementos) - set(aux)) - set(lista[x])))

    return A2

A1 = [[3, 4], [3], [4, 5], [4], [2], []]
A2 = complementar(A1)

print(A2)

