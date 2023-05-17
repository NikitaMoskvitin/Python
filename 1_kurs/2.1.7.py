def a(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return a(m-1,1)
    else:
        return a(m-1,a(m,n-1))
m = int(input())
n = int(input())
print(a(m,n))