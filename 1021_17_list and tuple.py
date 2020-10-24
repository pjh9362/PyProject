a = [1,2,3]
print(tuple(a))
print(a)
print(type(a))

b = tuple(a)
print(b)
print(type(b))

b = (4, 5, 6)
print(list(b))

c = list("Hello")
print(c)

a,b,c = [1,2,3]
print(a,b,c)

d,e,f = (4,5,6)
print(d,e,f)
print(type(a))
print(type(b))
print(type(d))
print(type(e))

x = [1,2,3]
a,b,c = x
print(a, b, c)

y = (4,5,6)
d,e,f = y
print(d,e,f)

'''
x =input().split()
print(x)
a, b = x
print(a, b)
'''

a = list(range(5, -10, -2))
print(a)
