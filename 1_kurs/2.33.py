a = [1,2,3]
b = [1,2,4]
c = dict(zip(a,b))
print(c)
d = {x:y for x,y in zip(a,b)}
print(d)
print( {x:y for x,y in zip(b,a)})