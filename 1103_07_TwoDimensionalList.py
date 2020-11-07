a = []

for i in range(10):
    a.append(0)

print(a)

l=[]
for i in range(3):
    temp = []
    for j in range(2):
        temp.append(0)
    l.append(temp)
print(l)

a = [[0 for j in range(2)] for i in range(3)]
print(a)

a = [[0]*2 for i in range(3)]
print(a)

print("\n****************************\n")

count = [3,1,3,2,5]
l = []

for c in count:
    l.append([0]*c)
print(l)

l=[]
for c in count:
    temp = []
    for i in range(c):
        temp.append(0)
    l.append(temp)
print(l)

a = [[0] * i for i in [3,1,3,2,5]]
print(a)

print("\n******************************\n")
a = [[10,20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)

print("\n******************************\n")
a = [[10,20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)

print("\n******************************\n")

a=[[10,20], [30,40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)

print("\n******************************\n")

a = [ [ [ 0 for col in range(3) ] for row in range(4)] for depth in range(2)]

print(a)
