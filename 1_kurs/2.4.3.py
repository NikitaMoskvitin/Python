a = list(map(int, input().split()))
a[0] = a.pop()
i = 0
def heap_down(a,i):
    if 2*i + 2 > len(a):
        return
    if 2*i + 3 > len(a):
        return
    if a[i] <= a[2*i + 1] and a[i] <= a[2*i+2]:
        return
    if a[i] > a[2*i + 1]:
        a[2*i + 1 ], a[i] = a[i], a[2*i + 1 ]
        k = 2*i + 1
        heap_down(a,k)
    if a[i] > a[2*i + 2]:
        a[2*i + 2 ], a[i] = a[i], a[2*i + 2 ]
        k = 2*i + 2
        heap_down(a,k)
heap_down(a,i)
print(a)

