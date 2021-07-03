def completo(M):

    for x in range(len(M)):
        for j in range(len(M)):
            if x == j:
                if M[x][j] != 0:
                    return False
            if x != j:
                if M[x][j] == 0:
                    return False
    return True


M = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

for x in range(len(M)):
    print(M[x])

if completo(M) == True:
    print("Completo")
else:
    print("Não é completo")


