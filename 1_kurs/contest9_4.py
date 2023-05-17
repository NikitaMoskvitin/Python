lst = input().split()
for i in range(0, len(lst)):
    lst[i] = int(lst[i])
a = max(lst)
for i in range(0,len(lst)):
    if lst[i] == a:
        b = i
print(a, b)