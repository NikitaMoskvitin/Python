import datetime
lst = list(map(int, input().split()))
def pyzirek(lst):
    for i in range(0, len(lst)):
        for j in range(0,len(lst)-1):
            if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst
def vibor(lst):
    for i in range(0,len(lst)):
        a = min(lst[i:])
        c = lst[i:].index(a)
        lst[i:][0], lst[i:][c] = lst[i:][c], lst[i:][0]
    return lst
def vstavka(lst):
    lst1 = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] >= lst1[len(lst1)-1]:
            lst1.append(lst[i])
        elif lst[i] <= lst1[0]:
            lst1.insert(0,lst[i])
        else:
            for j in range(0,len(lst1)-1):
                if lst1[j] < lst[i] and lst[i] < lst[j+1]:
                    lst1.insert(j+1,lst[i])
    return lst1
start_time = datetime.datetime.now()
print(pyzirek(lst))
print(datetime.datetime.now() - start_time)
start_time = datetime.datetime.now()
print(vibor(lst))
print(datetime.datetime.now() - start_time)
start_time = datetime.datetime.now()
print(vstavka(lst))
print(datetime.datetime.now() - start_time)