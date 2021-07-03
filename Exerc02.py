n = int(input("Insira o tamanho da matriz: "))

#quadrado = [[" "]* n] * n
quadrado = [[" " for _ in range(n)] for _ in range(n)]

for x in range(len(quadrado)):
    for j in range(len(quadrado)):
        if(j==0)  or (j == len(quadrado) - 1) or (x == 0) or (x == len(quadrado) - 1):
            quadrado[x][j] = "*"

for x in range(len(quadrado)):
    print("")
    for j in range(len((quadrado))):
        print(quadrado[x][j], end=" ")
        #print(x, j) remova essa linha para evitar quebras indesejadas