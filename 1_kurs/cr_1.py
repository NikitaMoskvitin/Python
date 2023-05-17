lst = list(map(int, input().split()))
a = max(lst)
i = lst.index(a)
lst.pop(i)
b = max(lst)
i = lst.index(b)
lst.pop(i)
if len(lst) >= 2:
    c = min(lst)
    i = lst.index(c)
    lst.pop(i)
    d = min(lst)
    i = lst.index(d)
    lst.pop(i)
    if a <= 0:
        print(c, d)
    elif a > 0 and b <= 0:
        print(c, d)
    elif b > 0 and d <= 0:
        if a * b >= c * d:
            print(b, a)
        else:
            print(c, d)
    elif d > 0:
        print(b, a)
elif len(lst) == 1:
    c = lst[0]
    if a <= 0:
        print(b, c)
    elif a > 0 and b <= 0:
        print(b, c)
    elif b > 0:
        print(b, a)
else:
    print(b, a)


