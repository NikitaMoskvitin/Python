from datetime import datetime
def Mach(N):
    lst = [0]*N
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        lst[0] = 1
        lst[1] = 2
        lst[2] = 4
        for i in range(3,N):
            lst[i] = lst[i-3] + lst[i-2] + lst[i-1]
        return lst[N-1]
N = int(input())
t1 = datetime.now()
print(Mach(N))
t2 = datetime.now()
print(t2-t1)