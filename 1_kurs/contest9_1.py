lst = input().split()
for i in range(0, len(lst)):
    lst[i] = int(lst[i])
lst.sort()
a = float('inf')
for i in range(0, len(lst)-1):
    if (lst[i+1] - lst[i]) < a:
        a = lst[i+1] - lst[i]
        b = i
print(lst[b], lst[b+1])