a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

a = []
print("before : ", a)
for i in range(0,10):
    a.append(i)
print("after : ", a)


a = []
print("before : ", a)
for i in range(10):
    a.append((i+1)*10)
print("after : ", a)

a = []
print("before : ", a)
for i in range(1, 101):
    if i%2==0:
        a.append(i)
print("after : ", a)

a = []
print("before : ", a)
for i in range(2, 101, 2):
    a.append(i)
print("after : ", a)

a = []
print("before : ", a)
for i in range(1,51):
    a.append(i*2)
print("after : ", a)

a=[10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(0, 500)
print(a)

a = [10, 20, 30]
a.insert(len(a), 500)
print(a)

a = [10, 20, 30]
a.insert(1, [500, 600])
print(a)

a = [10, 20, 30]
a[1:1] = [500, 600]
print(a)
