a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
lst = []
d = a
if c >= 0:
    while d < b:
        if d % 5 == 0:
            lst.append(d)
        d = d + c
else:
    while d > b:
        if d % 5 == 0:
            lst.append(d)
        d = d + c

if len(lst) > 0:
    print(int((sum(lst)/len(lst))//1))
    print(lst[len(lst)-1])
else:
    print(-1)
    print(0)
