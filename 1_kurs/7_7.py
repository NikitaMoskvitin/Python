m = int(input())
mas = []
for i in range(m):
    mas.append(list(map(int, input().split())))
for i in range(m):
    j = mas[i].index(min(mas[i]))
    mas1 = []
    for k in range(m):
        mas1.append(mas[k][j])
    if i == mas1.index(max(mas1)):
        print(mas[i][j])
        break
