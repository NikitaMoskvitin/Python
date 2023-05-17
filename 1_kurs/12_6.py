import math
k = int(input())
n = int(input())
if k >= n:
    print(k, '*', k)
else:
    if n % k == 0 and (math.sqrt(n/k))%1 == 0:
        print(int((n / k)), '*', int((n / k)))
    else:
        print(n, '*', n)