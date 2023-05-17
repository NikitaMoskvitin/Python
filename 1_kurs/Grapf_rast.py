G = [[0, 1, 2, 2, 3], [1, 0, 1, 1, 2], [2, 1, 0, 1, 1], [2, 1, 1, 0, 2], [3, 2, 1, 2, 0]]
V = ['A', 'B', 'C', 'D', 'E']
C = []
for i in range(len(G)):
    C.append(sum(G[i]))
m = min(C)
Cent = []
for i in range(len(C)):
    if C[i] == m:
        Cent.append(V[i])
DR = []
for i in range(len(G)):
    DR.append(max(G[i]))
R = min(DR)
D = max(DR)
print(Cent)
print(R)
print(D)