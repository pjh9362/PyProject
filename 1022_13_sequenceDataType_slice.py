a = list(range(0,100, 10))

a[2:5] = ['a', 'b', 'c']

print(a)

a = list(range(0, 100, 10))
print(a)
a[2:5] = ['a']
print(a)

print()
a = list(range(0, 100, 10))
print(a)
a[2:5] = ['a', 'b', 'c', 'd' , 'e']
print(a)


a = list(range(0, 100, 10))

a[2:8:2] = ['a' , 'b', 'c']
print(a)

a[2:8:2] = ['a', 'b']
print(a)
