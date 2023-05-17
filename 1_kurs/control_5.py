class Shtoto:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lst = []
        self.lst1 = []
        self.lst2 = []
        for i in range(0, self.a):
            self.lst.append(self.b)
            self.b = self.b + self.c
    def funct1(self, a, b, c):
        for i in range(0, len(self.lst)):
            if self.lst[i] % 2 == 0:
                self.lst1.append(self.lst[i])
        for i in range(0, len(self.lst1)):
            self.lst1[i] = str(self.lst1[i])
        r = '-'.join(self.lst1)
        print(r)
    def funct2(self,a,b,c):
        print(len(self.lst))
        print(min(self.lst))
        print(max(self.lst))
        print(max(self.lst)+min(self.lst))
    def funct3(self,a,b,c):
        for i in range(0, len(self.lst)):
            if self.lst[i] % 2 == 0:
                self.lst2.append(self.lst[i])
        print(sum(self.lst2))
    def funct4(self,a,b,c):
        c = int(input())
        print(self.lst.count(c))

cd = Shtoto(2, 4, 4)
cd.funct1(2, 4, 4)
cd.funct2(2, 4, 4)
cd.funct3(2, 4, 4)
cd.funct4(2, 4, 4)
