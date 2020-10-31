no = int(input("돌은 몇개 입니까?"))

stones=list(map(float, input().split()))

sum=0
for i in range(no):
    sum+=stones[i]

mean = sum/len(stones)

print(mean)

