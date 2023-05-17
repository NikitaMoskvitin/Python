a = float('-inf')
b = float('inf')
m = int(input())
mas = []
for i in range(m):
    mas.append(list(map(int, input().split())))
for i in range(len(mas)):
    for j in range(len(mas[i])):
        if mas[i][j] > a:
            a = mas[i][j]
            c =  i
        if mas[i][j] < b:
            b = mas[i][j]
            d = i
for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        print(mas[i][j], end=" ")
    print()
print('Минимум', b)
print('Максимум', a)
mas[d], mas[c] = mas[c], mas[d]
for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        print(mas[i][j], end=" ")
    print()
