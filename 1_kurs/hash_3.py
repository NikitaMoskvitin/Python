def _polinom_hash(_string, p , M):
    h = 0
    for i in range(len(_string)):
        h = h + ord(_string[i])*(p**(len(_string)- i - 1))
    h = h % M
    return h
def insert(a, key, value):
    h = _polinom_hash(key, 1, k)
    if a[h] == []:
        a[h].append(key)
        a[h].append(value)
    else:
        h = h + 1
        while a[h] != []:
            h = h + 1
        a[h].append(key)
        a[h].append(value)

def get(a, key):
    h = _polinom_hash(key, 1, k)
    if a[h] != []:
        if a[h][0] == key:
            return a[h][1]
        else:
            while a[h][0] != key:
                h = h + 1
                if a[h] == []:
                    while a[h] == []:
                        h = h + 1
            return a[h][1]
    else:
        h = h + 1
        while a[h] == []:
            h = h + 1
        if a[h][0] == key:
            return a[h][1]
        else:
            h = h + 1
            while a[h][0] != key:
                h = h + 1
            return a[h][1]

def errace(a, key):
    h = _polinom_hash(key, 1, k)
    if a[h] != []:
        if a[h][0] == key:
            a[h] = []
        else:
            while a[h][0] != key:
                h = h + 1
                if a[h] == []:
                    while a[h] == []:
                        h = h + 1
    else:
        h = h + 1
        while a[h] == []:
            h = h + 1
        if a[h][0] == key:
            a[h] = []
        else:
            h = h + 1
            while a[h][0] != key:
                h = h + 1
            a[h] = []

k = int(input())
a = [[] for i in range(k)]
while True:
    w = int(input())
    if w == 1:
        key, v = list(input().split())
        insert(a, key, v)
    elif w == 2:
        b = input()
        print(get(a, b))
    elif w == 3:
        b = input()
        errace(a, b)
