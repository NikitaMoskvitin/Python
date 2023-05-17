pole = [[0] * 8 for i in range(8)]
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
for i in range(8):
    pole[8-y1][i] = 1
    pole[i][x1-1] = 1
j = 8 - y1
for i in range(x1-1, 8):
    if j == 0:
        pole[j][i] = 1
        break
    else:
        pole[j][i] = 1
        j = j - 1
j = 8 - y1
for i in range(x1-1, 8):
    if j == 7:
        pole[j][i] = 1
        break
    else:
        pole[j][i] = 1
        j = j + 1
j = 8 - y1
for i in range(x1-1, -1, -1):
    if j == 0:
        pole[j][i] = 1
        break
    else:
        pole[j][i] = 1
        j = j - 1
j = 8 - y1
for i in range(x1-1, -1, -1):
    if j == 7:
        pole[j][i] = 1
        break
    else:
        pole[j][i] = 1
        j = j + 1
if pole[8-y2][x2-1] == 1:
    print('Может бить')
else:
    print('Не может бить')
pole[8-y2][x2-1] = 2
for i in range(0, len(pole)):
    for j in range(0, len(pole[i])):
        print(pole[i][j], end=" ")
    print()