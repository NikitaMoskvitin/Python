from _datetime import datetime
def Mach(N):

    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return Mach(N-3)+Mach(N-2)+Mach(N-1)
N = int(input())
t1 = datetime.now()
print(Mach(N))
t2 = datetime.now()
print(t2-t1)