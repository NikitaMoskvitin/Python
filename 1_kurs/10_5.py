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
obj = vect_matr() # создаем объект класса
print(obj.get()) # печатаем "взятый" вектор
n = obj.serch_n() # n = количество элементов, которые нужно добавить
obj.change_size(n) # меняем размер вектора и вводим недостающие значения
print(obj.get()) # печатаем "взятый" вектор нового размера
r = obj.separation() # делим вектор на новые векторы
for a in r:
  print(a) # печать полученных векторов
t = obj.unite(r) # объединяем векторы в матрицу
print(t) # печатаем матрицу
print(obj.min(t))
print(obj.msx(t))