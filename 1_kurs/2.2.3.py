from datetime import datetime
def Mach(N):
    lst = [0]*N
    if N == 0:
        return 0
    elif N == 1:
        return 2
    elif N == 2:
        return 4
    elif N == 3:
        return 7
    else:
        lst[0] = 2
        lst[1] = 4
        lst[2] = 7
        for i in range(3,N):
            lst[i] = lst[i-3] + lst[i-2] + lst[i-1]
        return lst[N-1]
N = int(input())
t1 = datetime.now()
print(Mach(N))