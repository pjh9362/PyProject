a = [0,0,0,0,0,0]
b=a

print(a is b)

b[2] = 99
print("a : ", a)
print("b : ", b)


print("\n***********************\n")

a=[0, 0, 0, 0, 0]
b = a.copy()

print(a is b)
print(a == b)

b[2] = 99
print("a :", a)
print("b :", b)
print(a == b)
