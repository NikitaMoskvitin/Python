m = int(input())
mas1 = []
for i in range(m):
    mas1.append(list(map(int, input().split())))
n = int(input())
mas2 = []
for i in range(n):
    mas2.append(list(map(int, input().split())))
mas = [[0] * len(mas2[0]) for i in range(len(mas1))]
for i in range(len(mas1)):
    for j in range(len(mas2[0])):
        c = 0
        for k in range(len(mas2)):
            c = c + (mas1[i][k] * mas2[k][j])
        mas[i][j] = c
for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        print(mas[i][j], end=" ")
    print()