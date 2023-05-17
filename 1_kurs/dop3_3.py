a = int(input())
b = [1, 1]
for i in range(2, 1001):
    b.append((b[i-1] + b[i-2]) % 10)
print(b[a])