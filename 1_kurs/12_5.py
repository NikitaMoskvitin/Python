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
print(k-1)