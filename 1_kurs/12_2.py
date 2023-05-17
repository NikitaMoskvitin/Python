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


s2 = 'abbaabbab'
print(s2)
pi = pref(s2)
print(pi)
s1 = 'aabaabaaaabaabаaab'
print(s1)
pi = pref(s1)
print(pi)
s3 = 'liilliil'
print(s3)
pi = pref(s3)
print(pi)
s4 = 'abcdabcabcdabcdab'
print(s4)
pi = pref(s4)
print(pi)
