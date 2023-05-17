def _polinom_hash(_string, p , M):
    h = 0
    for i in range(len(_string)):
        h = h + ord(_string[i])*(p**(len(_string)- i - 1))
    h = h % M
    return h
def Rabin_Karp(a, b):
    c = []
    h1 = _polinom_hash(a, 4, 1000)
    if len(b) - len(a) >= 0:
        for i in range(len(b) - len(a) + 1):
            d = b[i:i+len(a)]
            h2 =  _polinom_hash(d, 4, 1000)
            if h1 == h2:
                c.append(i)
        if c == []:
            c = [-1]
    else:
        c = [-1]
    return c
a = input()
b = input()
c = Rabin_Karp(a, b)
for i in range(len(c)):
    print(c[i], end=' ')