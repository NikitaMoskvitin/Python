import numpy as np
n = int(input())
m = int(input())
G = np.array([[0]*n for i in range(n)])
V = []
for i in range(n):
    V.append(i)
for i in range(m):
    b, c = map(int, input().split())
    G[b][c] = 1
    G[c][b] = 1
def Graph_glub(name, K, G):
    for i in V:
        if G[name][i] == 1:
            if i not in K:
                K.append(i)
                Graph_glub(i, K, G)
K = []
Graph_glub(V[0], K, G)
for i in range(len(K)):
    V.remove(K[i])
z = 1
while V != []:
    K = [V[0]]
    Graph_glub(V[0], K, G)
    for i in range(len(K)):
        V.remove(K[i])
    z = z + 1
o = 0
for i in range(len(G)):
    for j in range(len(G)):
        if G[i][j] == 1:
            g = G.copy()
            g[i][j] = 0
            g[j][i] = 0
            V = []
            for k in range(n):
                V.append(k)
            K = [V[0]]
            Graph_glub(V[0], K, g)
            for k in range(len(K)):
                V.remove(K[k])
            f = 1
            while V != []:
                K = [V[0]]
                Graph_glub(V[0], K, g)
                for k in range(len(K)):
                    V.remove(K[k])
                f = f + 1
            if f > z and j > i:
                print(i, j)
                o = 1
if o == 0:
    print(-1)