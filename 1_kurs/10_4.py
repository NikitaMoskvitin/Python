import numpy as np
class TwoMatrix:
    """Класс Матриц, определяет операции с матрицами"""
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def summ(self, a, b):
        return np.add(a, b)
    def raz(self, a, b):
        return np.subtract(a, b)
    def umn(self, a, b):
        return np.multiply(a,b)
    def dln(self, a, b):
        return np.divide(a, b)
    def trans(self, a, b):
        a = np.transpose(a)
        b = np.transpose(b)
        return a,b
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d = np.array([[223, 342, 4], [12, 32, 31], [31, 64, 64]])
f = TwoMatrix(c, d)
print(f.summ(c, d))
print(f.raz(c, d))
print(f.umn(c, d))
print(f.dln(c, d))
print(f.trans(c, d))
