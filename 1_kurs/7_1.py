class Matrix:
    """Класс матрицы"""
    def __init__(self):
        self.matr = []
    def get_matrix(self,n,m): #создание матрицы
        for i in range(n):
            self.matr.append([1]*m)
        return self.matr
    def dis(self): #для вывода матрицы
        return self.matr
    def in_matrix(self,n,m):
        for i in range(n):
            for j in range(m):
                self.matr[i][j] = int(input())
        return self.matr
mas = Matrix()
mas.get_matrix(3, 3)
print(mas.dis())
mas.in_matrix(3, 3)
print(mas.dis())
a = [[1, 2, 3], [5, 6, 7], [4, 8, 9]]
b = [[1, 2, 3],
     [1, 2, 3],
     [1, 5, 6]]
print(a)
print(b)
mas = [0] * 3
for i in range(3):
    mas[i] = [0] * 3
print(mas)
mas1 = []
for i in range(5):
    mas1.append([3] * 2)
print(mas1)
mas2 = [[3] * 4 for i in range(8)]
print(mas2)
for i in range(0, len(mas1)):
    for j in range(0, len(mas1[i])):
        print(mas1[i][j], end=" ")
    print()
for i in range(0, len(mas2)):
    for j in range(0, len(mas2[i])):
        print(mas2[i][j], end=" ")
    print()
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=" ")
    print()
for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        print(b[i][j], end=" ")
    print()
