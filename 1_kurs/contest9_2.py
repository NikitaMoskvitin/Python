lst1 = input().split()
lst2 = input().split()
lst3 = []
for i in range(0, len(lst1)):
    lst1[i] = int(lst1[i])
for i in range(0, len(lst2)):
    lst2[i] = int(lst2[i])
for i in range(0,len(lst1) + len(lst2)):
    if len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] >= lst2[0]:
            lst3.append(lst2[0])
            lst2.pop(0)
        else:
            lst3.append(lst1[0])
            lst1.pop(0)
    elif len(lst1) != 0 and len(lst2) == 0:
        for j in range(0, len(lst1)):
            lst3.append(lst1[j])
        break
    elif len(lst2) != 0 and len(lst1) == 0:
        for j in range(0, len(lst2)):
            lst3.append(lst2[j])
        break
print(*lst3)