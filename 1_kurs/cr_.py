def res(n):
    k=[0]*(n+1)
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 7
    else:
        k[1] = 2
        k[2] = 4
        k[3] = 7
        for i in range (4,n+1):
            k[i] = k[i-1] + k[i-2] + k[i-3]
    return k[n]
n=int(input())
print (res(n))