f = open('Graph_vz_or.txt')
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
print(G)