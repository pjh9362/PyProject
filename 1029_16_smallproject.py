Kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum=0
for i in Kor:
    sum+=i

mean = sum/len(Kor)
print(mean)

print("#######")

sum=0
i=0
while i<len(Kor):
    sum+=Kor[i]
    i+=1
mean=sum/len(Kor)
print(mean)
