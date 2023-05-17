import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
f = open('Graph.txt')
a = f.readline()
n, m = map(int,a.split())
G = [[0]*n for i in range(n)]
V = []
for i in range(m):
    a = f.readline()
    b, c = a.split()
    k = '-'
    d = '-'
    for j in range(len(V)):
        if V[j] == b:
            k = j
        if V[j] == c:
            d = j
    if k == '-':
        V.append(b)
        k = len(V) - 1
    if d == '-':
        V.append(c)
        d = len(V) - 1
    G[k][d] = 1
    G[d][k] = 1
def Graph_glub(name, K):
    for i in range(len(G)):
        if G[V.index(name)][i] == 1:
            if V[i] not in K:
                K.append(V[i])
                Graph_glub(V[i], K)
def Graph_shir(G):
    P = [V[0]]
    O = [V[0]]
    while len(P) != 0:
        x = P.pop(0)
        for i in range(n):
            if G[V.index(x)][i] == 1:
                if V[i] not in O:
                    P.append(V[i])
                    O.append(V[i])
    return O
for i in range(len(V)):
    V[i] = i
K = [V[0]]
Graph_glub(V[0], K)
print(K)
print(Graph_shir(G))
Z = nx.DiGraph(np.matrix(G))
nx.draw(Z, with_labels=True, node_size=300, arrows=True)
plt.show()

