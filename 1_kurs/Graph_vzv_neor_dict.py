f = open('Graph_vz.txt')
a = f.readline()
n, m = map(int,a.split())
G = {}
for i in range(m):
    a = f.readline()
    b, c, z= a.split()
    if G.get(b) == None:
        G.setdefault(b,{c:z})
    else:
        G[b].setdefault(c,z)
    if G.get(c) == None:
        G.setdefault(c,{b:z})
    else:
        G[c].setdefault(b,z)
print(G)