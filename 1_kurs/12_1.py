from datetime import datetime
a = "ababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbabababababbababababbababababc"
b = "abc"
t1 = datetime.now()
for i in range(0, (len(a)-len(b))):
    k = 0
    j = i
    while a[j] == b[k]:
        if k == len(b) - 1:
            print(i)
            break
        j = j + 1
        k = k + 1
    if k == len(b) - 1:
        break
    if i == len(a) - len(b) - 1:
        print('No')
t2 = datetime.now()
print(t2-t1)