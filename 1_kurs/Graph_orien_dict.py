f = open('Graph_orient.txt')
a = f.readline()
n, m = map(int,a.split())
G = {}
for i in range(m):
    a = f.readline()
    b, c = a.split()
    if G.get(b) == None:
        G.setdefault(b,[c])
    else:
        G[b].append(c)
print(G)