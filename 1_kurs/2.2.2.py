def Mach(N):
        lst = [0] * N
        if N == 0:
            return 0
        elif N == 2:
            return 1
        elif N == 2:
            return 3
        else:
            lst[0] = 2
            lst[1] = 3
            for i in range(2, N):
                lst[i] = lst[i - 2] + lst[i - 1]
            return lst[N - 1]
N = int(input())
print(Mach(N))