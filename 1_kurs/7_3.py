import array
m = int(input())
mas = []
for i in range(m):
    mas.append(list(map(int, input().split())))
c = array.array('i', [])
for i in range(len(mas)):
    d = 0
    for j in range(len(mas[i])):
        d = d + mas[i][j]
    c.append(d)
j = 0
d = 0
for i in range(len(mas)):
    d = d + mas[i][j]
    j = j + 1
c.append(d)
j = 0
d = 0
for i in range(len(mas)-1, -1, -1):
    d = d + mas[i][j]
    j = j + 1
c.append(d)
print(c)