def busca_profundidade(G, s):

    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    count = 0
    conexo = 0

    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in G[u]:
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break
            if desempilhar :
                S.pop()
        print(len(S))

    for v in desc:
        if desc[v] == 0:
            count+= count
            for x in G[v]:
                for y in desc:
                    if x == y:
                        conexo += conexo

    if conexo == count:
        return print("Conexo")
    else:
        return print("Desconexo")


