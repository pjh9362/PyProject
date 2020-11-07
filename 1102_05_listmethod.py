a=[10, 20, 30, 15, 20, 40]
print(a.count(20))
print(a)
a.reverse()
print(a)

a.sort()
print("After sort()")
print(a)

a.sort(reverse = True)
print("After sort(reverse = True)")
print(a)

a = [10, 20, 30]
print(a)
a.clear()
print(a)

a = [10, 20, 30]
print(a)
del a[:]
print(a)

a = [10, 20, 30]
a[len(a):] = [500]
print(a)

a = [10, 20, 30]
a[len(a):] = [500, 600]
print(a)
