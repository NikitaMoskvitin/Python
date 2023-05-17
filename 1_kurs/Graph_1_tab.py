n, m = map(int, input().split())
G = [[0]*n for i in range(n)]
V = []
for i in range(n):
    V.append(i)
for i in range(m):
    b, c = map(int, input().split())
    G[b][c] = 1
    G[c][b] = 1
def Graph_shir(G):
    P = [V[0], 'd']
    O = [V[0], 'd']
    while len(P) != 0:
        x = P.pop(0)
        if x == 'd':
            O.append('d')
            x = P.pop(0)
        for i in range(n):
            if G[V.index(x)][i] == 1:
                if V[i] not in O:
                    P.append(V[i])
                    O.append(V[i])
    return O
O = Graph_shir(G)
for i in range(n):
    d = O[:O.index(i)]
    print(d.count('d'))