class Four_corners:
    """класс четырехугольников"""
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimetr(self, a, b, c, d):
        return a + b + c + d
class Rect(Four_corners):
    """Класс прямоугольников"""
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
    def plos(self, a ,b):
        return a * b
class Quatro(Four_corners):
    """Класс квадратов"""
    def __init__(self,a):
        super().__init__(a, a, a, a)
    def plos(self, a):
        return a * a
class Trap(Four_corners):
    """Класс трапеции"""
    def __init__(self, a, c, h):
        super().__init__(a, c, a, c)
        self.h = h
    def plos(self, a, c, h):
        return ((a + c) / 2) * h
r1 = Four_corners(1, 2 , 3 , 4)
print(r1.perimetr(1, 2, 3, 4))
r2 = Rect(1, 2)
print(r2.plos(1, 2))
print(r2.perimetr(1, 2, 1, 2))
r3 = Quatro(1)
print(r3.plos(1))
print(r3.perimetr(1, 1, 1, 1))
r4 = Trap(1, 2, 3)
print(r4.plos(1, 2, 3))