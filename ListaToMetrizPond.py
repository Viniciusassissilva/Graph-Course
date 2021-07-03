
def retornaMatriz(lista):

    M = [[" " for _ in range(len(A))] for _ in range(len(A))]

    for x in range(len(lista)):
        ref = 0
        aux = lista[x][ref]
        print(aux)
        for j in range(len(lista)):
            if j == aux[0]:
                M[x][j] = aux[1]
                if ref + 1 < len(lista[x]):
                    aux = lista[x][ref + 1]
            else:
                M[x][j] = 0

    return M

A = [[(1, 2), (2, 2)], [(0, 1), (2, 1)], [(0, 3), (1, 3)]]
print(A)
M = retornaMatriz(A)

for x in range(len(M)):
    print(M[x])