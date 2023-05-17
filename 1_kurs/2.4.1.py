a = list(map(int,input().split()))
c = 1
for i in range((len(a)-1),0,-1):
    if a[(i - 1)//2] <= a[i]:
        continue
    else:
        c = 0
        break
print(b)