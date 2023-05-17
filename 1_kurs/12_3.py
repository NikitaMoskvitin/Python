from datetime import datetime
def pref(s):
    pi = [0]*len(s)
    print(len(s))
    j = 0
    i = 1
    pi[0] = 0
    while i < len(s):
        if s[i] != s[j]:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j-1]
        else:
            pi[i] = j + 1
            j += 1
            i += 1
    return pi
a = input()
b = input()
t1 = datetime.now()
c = b + "@" + a
pi = pref(c)
pi = pi[len(b)+1:]
print(pi)
j = 0
while len(pi) != 0:
    k = pi.index(len(b)) +1
    print(j + pi.index(len(b)))
    pi = pi[k:]
    j = j + k
t2 = datetime.now()
