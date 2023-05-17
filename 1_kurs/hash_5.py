def _hash(_string, M):
    h = 0
    for i in range(len(_string)):
        h = h + ord(_string[i])
    h = h % M
    return h

_string = input()
M = int(input())
print(_hash(_string, M))