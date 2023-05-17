m = int(input())
mas = []
for i in range(m):
    mas.append(list(map(int, input().split())))
def first_last(letter, st):
    if mas[st].count(letter) == 0:
        a = [None, None]
    elif mas[st].count(letter) == 1:
        a = [mas[st].index(letter), mas[st].index(letter)]
    else:
        a = []
        c = mas[st].index(letter)
        a.append(c)
        mas[st].reverse()
        a.append(len(mas[st]) - 1 - mas[st].index(letter))
    return a
letter = int(input())
st = int(input())
print(first_last(letter, st))