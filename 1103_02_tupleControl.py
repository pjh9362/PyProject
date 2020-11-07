a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

a = (10, 20, 30, 15, 20, 40)
print(a.count(20))

a = (38, 21, 53, 62, 19)

for i in a:
    print(i, end=' ')
print()

i=0
while i<len(a):
    print(a[i], end = ' ')
    i+=1
print()

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))

a = tuple(map(str, input().split()))
print(a)
print(min(a))
print(max(a))
