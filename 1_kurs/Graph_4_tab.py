n, m = map(int,input().split())
G = [[0]*n for i in range(n)]
V = []
for i in range(n):
    V.append(i)
for i in range(m):
    b, c = map(int,input().split())
    G[b][c] = 1
def Graph_glub(name, K, P):
    for i in range(len(G)):
        if G[V.index(name)][i] == 1:
            if V[i] not in K:
                K.append(V[i])
                Graph_glub(V[i], K, P)
                P.insert(0, V[i])
K = []
P = []
Graph_glub(V[0], K, P)
print(P)