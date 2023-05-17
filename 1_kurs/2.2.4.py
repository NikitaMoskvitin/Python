import random
n = int(input())
def pir(n):
    b = [random.randrange(1,n+1,1) for i in range(n)]
    if n == 1:
        print(b)
        return b[0]
    elif n == 2:
        print(b)
        return b[1]
    else:
        sum = 0
        i = 0
        while i < n - 1:
            if b[i] < b[i+1]:
                sum = sum + b[i]
                i = i + 1
            else:
                sum = sum + b[i+1]
                i = i + 2
        print(b)
    return sum
print(pir(n))