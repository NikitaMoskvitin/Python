from pythonds.basic import Stack as S

def pechat(s):
    a = s
    while a.isEmpty is not True:
        print(a.pop())
s = S()
print(s.isEmpty())
s.push(input())
s.push(input())
print(s.size())

s.peek()
print(s.pop())

