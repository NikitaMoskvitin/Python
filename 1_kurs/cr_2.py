n = int(input())
lst = []
if n == 1:
    lst = [1]
elif n == 2:
    lst = [1, 3]
else:
    lst = [1, 2]
    for i in range(2, n):
        lst.append(lst[i-2] + lst[i-1])
b = 0
for i in range(len(lst)):
    if lst[i]%2 == 0:
        b = b + lst[i]
print(b)