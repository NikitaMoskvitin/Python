m = int(input())
mas = []
for i in range(m):
    mas.append(list(map(int, input().split())))
for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        print(mas[i][j], end=" ")
    print()
for i in range(m):
    for j in range(i, m):
        mas[i][j], mas[j][i] = mas[j][i], mas[i][j]
for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        print(mas[i][j], end=" ")
    print()