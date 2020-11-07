a = [[10, 20], [30, 40], [50, 60]]
print(a)


a = [[10, 20],
     [30, 40],
     [50, 60]]
print(a)

print("\n*************************\n")

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

print("\n*************************\n")

print(a[0][0])
print(a[1][1])
print(a[2][1])
a[0][1]=1000
print(a[0][1])

print("\n*************************\n")

a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

print("\n*************************\n")

for aa in a:
    for aaa in aa:
        print(aaa, end = ' ')
    print()
    
print("\n*************************\n")

for x,y in a:
    print(x,y)

print("\n*************************\n")

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

print("\n*************************\n")

i=0
while i<len(a):
    x, y = a[i]
    print(x, y)
    i+=1

print("\n*************************\n")

i = 0
while i<len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1
    
print("\n*************************\n")

a = [[1,2,3], [5,6,7], [8,9,10], [12,13,14]]
for x,y,z in a:
    print(x,y,z)

print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

print()

i=0
for i in range(len(a)):
    j = 0
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
        j+=1
    print()
    i+=1

print()

i=0
while i < len(a):
    x,y,z = a[i]
    print(x, y, z)
    i+=1
