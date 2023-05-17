a = list(map(int, input().split()))
b = int(input())
a.append(b)
i = len(a) - 1
def heap_up(a, i):
    if len(a) == 1:
        return
    if i == 0:
        return
    if a[i] < a[( i - 1 )//2]:
        a[(i - 1) // 2], a[i] = a[i], a[(i-1)//2]
        k = (i-1) // 2
        heap_up(a,k)
heap_up(a, i)
print(a)