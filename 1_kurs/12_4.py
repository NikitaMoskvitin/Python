lst = list(map(int, input().split()))
lst.sort()
lst1 = lst
a = int(input())
k = 0
while len(lst) != 1:
    j = len(lst) // 2
    if lst[j-1] < a:
        lst = lst[j:]
        k = k + j
    elif lst[j-1] >= a:
        lst = lst[:j]
f = 0
while len(lst1) != 1:
    j = len(lst1) // 2
    if lst1[j] <= a:
        lst1 = lst1[j:]
        f = f + j
    elif lst1[j] > a:
        lst1 = lst1[:j]
if f ==k:
    print(k)
else:
    print(k, f)
