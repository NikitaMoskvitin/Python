n, m, S, F = map(int, input().split())
G = [[0]*n for i in range(n)]
V = []
for i in range(m):
    b, c, z = map(int, input().split())
    z = int(z)
    G[b][c] = z
    G[c][b] = z
dict_ = {}
dict_.setdefault(S, 0)
for i in range(len(G)):
    dict_.setdefault(i, float('+inf'))

Stack = []
Stack.append(S)
for i in range(len(G)):
    if G[S][i] != 0:
        Stack.append(i)
        dict_[i] = G[S][i]
V = [S]
Stack.pop(0)
while len(Stack) != 0:
    k = Stack.pop(0)
    V.append(k)
    for i in range(len(G)):
        if G[k][i] != 0:
            if i not in V:
                Stack.append(i)
            if dict_[i] > dict_[k] + G[k][i]:
                dict_[i] = G[k][i] + dict_[k]
R = [F]
for i in range(len(G)):
    if G[F][i] != 0:
        if dict_[i] < dict_[F]:
            R.append(i)
R.append(0)
print(dict_)
print(dict_[F])
