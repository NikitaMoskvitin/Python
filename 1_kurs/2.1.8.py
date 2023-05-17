def matreshka(n):
    if n == 1:
        print("матрешка")
    else:
        print("верх матрешки",n)
        matreshka(n-1)
        print("низ матрешки",n)
n = int(input())
matreshka(n)
