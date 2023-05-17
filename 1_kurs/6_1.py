class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        print("Работает конструктор класса Point")
    def multiplication(self):
        print(self.x1 * self.y1)
class Rect(Point):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2
        print("Работает конструктор класса Rect")
    def area(self, x1, y1, x2, y2):
        return (abs((x2 - x1)) * abs((y2 - y1)))
class Coordx(Point):
    def __init__(self,x1):
        super().__init__(x1, x1)
        print("Работает конструктор класса Coordx")
    def pech(self, x1):
        print(x1)
class Trangle(Point):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def sush(self, x1, y1, x2, y2, x3, y3):
        a = (abs(x1 - x2) * abs(x1 - x2) + abs(y1 - y2) * abs(y1 - y2)) ** (1 / 2)
        b = (abs(x1 - x3) * abs(x1 - x3) + abs(y1 - y3) * abs(y1 - y3)) ** (1 / 2)
        c = (abs(x2 - x3) * abs(x2 - x3) + abs(y2 - y3) * abs(y2 - y3)) ** (1 / 2)
        if (a + b) > c:
            if (b + c) > a:
                if (a + c) > b:
                    print("Cущесвует")
                else:
                    print("Не сущесвует")
            else:
                print("Не сущесвтует")
        else:
            print("Не сущесвует")
r1 = Point(1, 2)
r1.multiplication()
r2 = Rect(1, 2, 3, 4)
r2.multiplication()
print(r2.area(1, 2, 3, 4))
r3 = Coordx(1)
r3.multiplication()
r3.pech(1)
r4 = Trangle(1, 2, 3, 4, 5, 6)
r4.multiplication()
r4.sush(1, 2, 3, 4, 5, 6)
