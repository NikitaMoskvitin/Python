def _polinom_hash(_string, p , M):
    h = 0
    for i in range(len(_string)):
        h = h + ord(_string[i])*(p**(len(_string)- i - 1))
    h = h % M
    return h

k = list(map(int, input().split()))
p , M = k
_string = input()
print( _polinom_hash(_string, p, M))

