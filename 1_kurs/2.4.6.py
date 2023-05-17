a = list(map(int,input().split()))
def heap_up_min(a, i):
    if len(a) == 1:
        return
    if i == 0:
        return
    if a[i] < a[( i - 1 )//2]:
        a[(i - 1) // 2], a[i] = a[i], a[(i-1)//2]
        k = (i-1) // 2
        heap_up_min(a,k)

def heap_up_max(a, i):
    if len(a) == 1:
        return
    if i == 0:
        return
    if a[i] > a[( i - 1 )//2]:
        a[(i - 1) // 2], a[i] = a[i], a[(i-1)//2]
        k = (i-1) // 2
        heap_up_max(a,k)

k_min = []

for j in range(len(a)):
    k_min.append(a[j])
    i = len(k_min) - 1
    heap_up_min(k_min, i)

k_max = []

for j in range(len(a)):
    k_max.append(a[j])
    i = len(k_max) - 1
    heap_up_max(k_max, i)

print(k_min)

print(k_max)

