import numpy as np
class vect_matr:
  '''класс - одномерный массив, ввести, добавить, разбить, сделать матрицу'''
  def __init__ (self): # конструктор. вод элементов вектора
    self.vector = np.array(list(map(int, input().split())))

  def get(self):
    return self.vector # взятие значения вектора

  def serch_n(self):
    k=len(self.vector)
    n= 3 - k%3 # определение количества, элементов, которые нужно добавить
    return n

  def change_size(self, n): # изменение размера вектора и ввод недостающих значений
    k = len(self.vector)
    self.vector = np.resize(self.vector, k + n)
    print("введите", n, "новых элемента вектора")
    for i in range(n):
      self.vector[k+i] = int(input())

  def separation(self): # разделение вектора на 3 вектора
    self.p = np.split(self.vector,3) # vector не изменяется, возвращаем новые векторы
    return self.p

  def unite(self,p): # объединение полученных векторов в матрицу
    self.t = np.vstack(self.p) # vector не изменяется, возвращаем новую матрицу
    return self.t
  def min(self,t):
    return t.min()
  def msx(self,t):
    return t.max()
x = vect_matr()
y = vect_matr()
dot_product = 0
for a, b in zip(x.get(), y.get()):
  dot_product += a * b
print(dot_product)
r1 = x.separation()
c = x.unite(r1)
r2 = y.separation()
d = y.unite(r2)
print(np.dot(c,d))
print(np.linalg.inv(c))
print(np.dot(c, np.linalg.inv(c)))