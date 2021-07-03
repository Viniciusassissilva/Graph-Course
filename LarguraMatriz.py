def busca_largura(G, s):

    desc = [0 for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1

    while len(Q) != 0:

        u = Q.pop(0)
        for v in range(len(G)):
            if G[u][v] == 1:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1

    return R