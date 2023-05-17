lst = [i*i for i in range(1, 21)]
print(lst)
lst[9] = 50
print(lst)
for i in range(0, 20):
    if lst[i] % 2 == 0:
        lst[i] = 1
print(lst)
for i in range(0, 20):
    if i % 2 == 1:
        lst[i] = lst[i] / 2
lst1 = lst
print(lst)
for a in range(0, 20):
    for i in range(0, 19):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)
print("минмальное значение", lst[0])
print("максимальное значение", lst[19])
b=0
for i in range(0, 20):
    b = b + lst[i]
print("сумма", b)
print(sum(lst))
print(min(lst))
print(max(lst))
print(sorted(lst1))