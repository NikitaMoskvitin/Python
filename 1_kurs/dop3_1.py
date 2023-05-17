a = int(input())
b = [1, 1]
for i in range(2, 45):
    b.append(b[i-1] + b[i-2])
print(b[a-1])
