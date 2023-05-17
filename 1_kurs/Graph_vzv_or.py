import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
f = open('Graph_vz_or.txt')
a = f.readline()
n, m = map(int,a.split())
G = [[0]*n for i in range(n)]
V = []
for i in range(m):
    a = f.readline()
    b, c, z = a.split()
    k = '-'
    d = '-'
    z = int(z)
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
    G[k][d] = z
for i in range(n):
    for j in range(n):
        print(G[i][j], end= ' ')
    print(end='\n')
Z = nx.DiGraph(np.matrix(G))
nx.draw(Z, with_labels=True, node_size=300, arrows=True)
plt.show()