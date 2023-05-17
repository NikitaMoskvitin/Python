f = open('Graph.txt')
a = f.readline()
n, m = map(int,a.split())
G = [[] for i in range(n)]
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
    G[d].append(V.index(b))
    G[k].append(V.index(c))
print(G)
for i in range(n):
    print(i, end= ' ')
    print(len(G[i]), end=' ')
    print(G[i])