def Proove(d,n):
    if n in d:
        return True
    else:
        return False
n = int(input())
d = {1:2, 3:4}
print(Proove(d,n))