
def retornaMatriz(lista):

    M = [[0 for _ in range(len(A))] for _ in range(len(A))]

    for x in range(len(lista)):
        for j in range(len(lista[x])):
            M[x][lista[x][j]] = 1

    return M

A = [[3, 4], [3], [5, 4], [4], [2], [0, 1]]

M = retornaMatriz(A)

for x in range(len(M)):
    print(M[x])