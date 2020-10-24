a = [1,2,3]
b = 4,5

#print(a+b) -> list + tuple => error!!!

print(a+list(b))

print("********************")

a = [1,2]
b = [3, 4]
c = a+b

print(a+b)
print(a)
print(b)
print(c)
