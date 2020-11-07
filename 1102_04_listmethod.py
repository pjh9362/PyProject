a = [10, 20, 30, 15, 20, 40]
print(a.index(20))

print()

a=[10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]

index = []

for i in range(len(a)):
    if a[i]==20:
        index.append(i)

print(index)



a=[10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]

index = []

for i in range(len(a)):
    if a.pop() == 20:
        index.append(i)


#reference
a=[10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]

index = []

while 20 in a:
    index.append(a.index(20)+len(index))
    a.remove(20)


#answer1
add=0
a=[10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
result = []

while 20 in a:
    i = a.index(20);
    result.append(i + add)
    a.pop(i)
    add+=1
    
print(result)
