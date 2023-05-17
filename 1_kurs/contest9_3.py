a = int(input())
lst = [True]*100001
lst[0] = False
lst[1] = False
for i in range(2, len(lst)):
    if lst[i] == True:
        for j in range(2*i, len(lst), i):
            if j % i == 0 :
                lst[j] = False
b = 0
c = 0
lst.index(False)
for i in range(2, len(lst)):
    if lst[i] == True:
        b = b + 1
        c = i
        if b == a:
            break
print(c)