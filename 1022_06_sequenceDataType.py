print(list(range(0,5,2))*3)

print(tuple(range(0,5,2))*3)

print("Hello, "*3)

#print(range(0,5,2)*3) -> TypeError: unsupported operand type(s) for *: 'range' and 'int'

print()

a = list(range(0, 100, 10))

print(a)
print(len(a))

b = tuple(range(0, 10, 2))
print(b)
print(len(b))

c = range(0, 10 , 2)
print(len(c))
