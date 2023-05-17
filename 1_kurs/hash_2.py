class Zveno:

    '''Класс звеньев'''

    def __init__(self, data, key):
        self.value = data
        self.key = key
        self.next = None

class Spisoc:

    '''Класс списков'''

    def __init__(self):
        self.head = None

    def dob_v_nachalo(self, b, a,):

        '''Функция добаляет элемент в начало'''


        current = Zveno(a, b)
        current.next = self.head
        self.head = current

    def dob_v_conec(self, b, a):

        '''Функция добовляет элемент в конец'''

        current = self.head
        while current != None:
            prev = current
            current = current.next
        current = Zveno(a, b)
        prev.next = current

    def vstavka_posl(self):

        '''Функция добовляет элемент послк элемента с введеным значением'''

        a = input()
        current = self.head
        while current.value != a:
            prev = current
            current = current.next
        prev = current
        b = input()
        current = Zveno(b)
        current.next = prev.next
        prev.next = current

    def udol_nachalo(self):

        '''Функция удаляет начальный элемент'''

        prev = self.head
        current = prev.next
        self.head = current

    def udol_conec(self):

        '''Функция удаляет последний элемент'''

        current = self.head
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None

    def udol_posl(self, a):

        '''Функция удаляет элемент с введеным значением'''

        current = self.head
        while current.key != a:
            prev = current
            current = current.next
        prev.next = current.next

    def pechat(self):

        '''Функция печаете список'''

        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def udol(self):

        '''Функция удаляет список'''

        self.head = None

    def poisk(self, b):

        '''Функция ищеит элемент'''

        current = self.head
        z = None
        while True:
            if current.key == b:
                z = current.value
                break
            current = current.next
        return z

def _polinom_hash(_string, p , M):
    h = 0
    for i in range(len(_string)):
        h = h + ord(_string[i])*(p**(len(_string)- i - 1))
    h = h % M
    return h

def _create_table(k):
    a = [Spisoc() for i in range(k)]
    return a

def insert(b, a, k, c):
    h = _polinom_hash(b, 1, k)
    if c[h].head == None:
         c[h].dob_v_nachalo(b, a)
    else:
        c[h].dob_v_conec(b, a)
    return c
def get(b, c, k):
    h = _polinom_hash(b, 1, k)
    value = c[h].poisk(b)
    return value

def errase(b, c, k):
    h = _polinom_hash(b, 1, k)
    if c[h].head.key == b:
        c[h].udol_nachalo()
    else:
        c[h].udol_posl(b)

k = int(input())
c = _create_table(k)
while True:
    w = int(input())
    if w == 1:
        b, a = list(input().split())
        insert(b, a, k, c)
    elif w == 2:
        b = input()
        print(get(b, c ,k))
    elif w == 3:
        b = input()
        errase(b, c, k)