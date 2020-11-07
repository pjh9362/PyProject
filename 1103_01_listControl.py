a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

'''
a = input().split()
print(a)

a = map(int, input().split())
print(a)
a = list(a)
print(a)
'''

a, b = [10, 20]
print(a)
print(b)

a, b = map(int, input().split())
print(a)
print(b)
