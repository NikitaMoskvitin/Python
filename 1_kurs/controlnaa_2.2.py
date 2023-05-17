def dvich(n):
    d = 0
    lst = [i for i in n]
    for i in range(0, len(lst)):
        if lst[i] == '1':
            lst[i] = '0'
        elif lst[i] == '0':
            lst[i] = '1'
    for i in range(0, len(lst)):
        b = int(lst[i])
        c = b*(2**(len(lst)-1-i))
        d = d + c
    print(d)
n = str(input())
dvich(n)
