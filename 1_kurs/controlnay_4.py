class Student:
    def __init__(self, student_name):
        self.student_name = student_name
        self.marks = []
    def ImOz(self,student_name,marks): # имя + макс оценка
        print(self.student_name)
        print(max(self.marks))
    def Sred(self,marks): # средняя оценка
        print(sum(self.marks)/len(self.marks))
    def Obmen(self,marks): # замена оценки( i - индекс, j - на что заменить хотим)
        i = int(input())
        j = int(input())
        self.marks[i] = j
a = Student('Никита')
a.marks = [3, 5, 10, 7]
a.ImOz(a.student_name, a.marks)
a.Sred(a.marks)
a.Obmen(a.marks)
print(a.marks)


