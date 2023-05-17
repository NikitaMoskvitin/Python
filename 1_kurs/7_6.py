m = int(input())
a = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
for i in range(3):
    for j in range(3):
        a[i][j] = a[i][j] + (m // 3) - 5
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=" ")
    print()