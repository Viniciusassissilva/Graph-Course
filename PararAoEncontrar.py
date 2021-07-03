def busca_profundidade_rec(G, s, x):
    R.append(s)
    desc[s] = 1
    for v in G[s]:
        if v == x:
            R.append(x)
            return R
        if desc[v] == 0:
            busca_profundidade_rec(G, v, x)
    if x == R[len(R)-1]:
        return R
    else:
        R.pop()
        return R

A = [[3, 5, 6], [4], [4, 1], [6], [], [7], [8], [1], []]
desc = [0 for i in range(len(A))]
R = []

print(busca_profundidade_rec(A, 0, 5))