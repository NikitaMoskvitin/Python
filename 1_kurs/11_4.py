a = input()
b = input()
lst1 = list(a)
lst2 = list(b)
lst1[1], lst2[4] = lst2[4], lst1[1]
lst1[2], lst2[5] = lst2[5], lst1[2]
lst1[3], lst2[6] = lst2[6], lst1[3]
a = ''.join(lst1)
b = ''.join(lst2)
print(a)
print(b)