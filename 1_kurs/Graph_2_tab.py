n = int(input())
m = int(input())
G = [[0]*n for i in range(n)]
V = []
for i in range(n):
    V.append(i)
for i in range(m):
    b, c = map(int, input().split())
    G[b][c] = 1
    G[c][b] = 1
def Graph_glub(name, K):
    for i in V:
        if G[name][i] == 1:
            if i not in K:
                K.append(i)
                Graph_glub(i, K)
K = []
Graph_glub(0, K)
for i in range(len(K)):
    V.remove(K[i])
z = 1
while V != []:
    K = [V[0]]
    Graph_glub(V[0], K)
    for i in range(len(K)):
        V.remove(K[i])
    z = z + 1
print(z)