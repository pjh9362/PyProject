a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)

c = [ i + 5 for i in range(10)]
print(c)

d = [i * 2 for i in range(10)]
print(d)
d = []
for i in range(10):
    d.append(i*2)
print(d)


a = [i for i in range(10) if i%2 == 0]
print(a)

b = [ i + 5 for i in range(10) if i%2==1]
print(b)

c = [ i*j for i in range(2, 10) for j in range(1,10)]
print(c)
