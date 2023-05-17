n, m = map(int, input().split())
G = [[0]*n for i in range(n)]
V = []
for i in range(n):
    V.append(i)
for i in range(m):
    b, c, z = map(int, input().split())
    G[b][c] = z
    G[c][b] = z
def Graph_glub(name, K):
    for i in V:
        if G[name][i] != 0:
            if i not in K:
                K.append(i)
                Graph_glub(i, K)
K = []
Graph_glub(0, K)
sum = 0
for i in range(len(K)):
    for j in range(len(K)):
        sum = sum + G[i][j]
for i in range(len(K)):
    V.remove(K[i])
H = []
H.append(sum//2)
while V != []:
    K = [V[0]]
    Graph_glub(V[0], K)
    sum_ = 0
    for i in K:
        for j in K:
            sum_ = sum_ + G[i][j]
    H.append(sum_//2)
    for i in range(len(K)):
        V.remove(K[i])
H.sort()
for i in range(len(H)):
    print(H[i])
