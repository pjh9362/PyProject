a = [10, 20, 30, 40, 20, 50, 20, 30, 60, 70, 20]
result=[]

for index, value in enumerate(a):
    if value == 20:
        result.append(index)

print(result)

a = [38, 21, 53, 62, 19]
i = 0
while i < len(a): #i<=len(a) -> IndexError: list index out of range
    print(a[i])
    i+=1

a.sort()
print("smallest : ", a[0])
a.sort(reverse = True)
print("largest : ", a[0])

a = [38, 21, 53, 62, 19]
print(min(a))
print(max(a))

#합계 구하기
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x+=i
print(x)
print(sum(a))

b = ['a', 'b', 'c' ,'d', 'e', 'f', 'g']
print(sum(b))
