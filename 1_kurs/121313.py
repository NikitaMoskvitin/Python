n = '1010'
lst = [i for i in n]
for i in range(0,len(lst)):
        if lst[i] == '1':
          lst[i] = '0'
        else:
            lst[i] == '1'
a = sum(lst)
b = int(a)
print(b)