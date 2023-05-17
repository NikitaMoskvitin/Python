a = int(input())
b = [1, 2, 4]
for i in range(3, 31):
    b.append(b[i-1] + b[i-2] + b[i-3])
print(b[a-1])