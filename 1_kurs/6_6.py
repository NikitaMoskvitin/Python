lst = input().split()
a = float('-inf')
c = float('inf')
for i in range(0, len(lst)):
    lst[i] = int(lst[i])
    if a < lst[i]:
        a = lst[i]
        b = i
for i in range(0, len(lst)):
    if c > lst[i]:
        c = lst[i]
        d = i
print("Максимум", a)
print(max(lst))
print("Минимум", c)
print(min(lst))
print(lst)
lst[b], lst[d] = lst[d], lst[b]
print(lst)

