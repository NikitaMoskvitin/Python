lst = input().split()
for i in range(0, len(lst)):
    lst[i] = int(lst[i])
lst1 = []
lst3 = []
b = float('-inf')
for i in range(0, len(lst)-1):
    lst1.append(lst[i+1] - lst[i])
lst2 = lst1
while len(lst1) != 0:
    i = 0
    if len(lst1) == 1:
        break
    else:
        while lst1[i+1] - lst1[i] == 0:
            i = i + 1
            if i + 1 == len(lst1):
                break
        if i > b:
            b = i
            c = lst1[0]
        lst1 = lst1[i+1:]
for i in range(lst2.index(c),lst2.index(c) + b + 2):
    lst3.append(lst[i])
print(lst3)
