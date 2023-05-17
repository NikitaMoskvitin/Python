lst = [True]*10000
lst[0] = False
lst[1] = False
for i in range(2, len(lst)):
    if lst[i] == True:
        for j in range(2*i, len(lst), i):
            if j % i == 0 :
                lst[j] = False
lst2 = []
for i in range(0, len(lst)):
    if lst[i] == True:
        lst2.append(i)
print(lst2)
