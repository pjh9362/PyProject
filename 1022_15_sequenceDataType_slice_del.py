a = list(range(0, 100, 10))
print(a)

#del a[2:5]
del a[2:8:2]

print(a)


print()

b = tuple(range(0, 100, 10))
print(b)

#del b[2:5]

#TypeError: 'tuple' object does not support item deletion


print()

r = range(10)
print(r)

#del r[2:5]
#TypeError: 'range' object does not support item deletion

print()

hello = 'Hello, world!'
#del hello[2:9]
