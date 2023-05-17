lst = list(map(int, input().split()))
a = float("inf")
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        b = lst[i] + lst[i+1]
        if b < a:
            a = b
            c = i
print(lst[c], lst[c+1])