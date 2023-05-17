n = int(input())
lst = []
if n == 1:
    lst = [0]
elif n == 2:
    lst = [0, 1]
else:
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i-2] + lst[i-1])
r = lst[0]+lst[len(lst)-1]
print(r)
if r == 2:
    print(3)
if r == 0:
    print(0)
if r == 5:
    print()
