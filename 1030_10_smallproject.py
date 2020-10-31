Scores = list(map(int,input("실기점수를 입력하세요 : ").split()))

min=100
max=0

sum=0

'''
for i in Scores:
    if min>i:
        min=i
    if max<i:
        max=i
    sum+=i
'''

for i in Scores:
    sum+=i

for i in Scores:
    if max<i:
        max=i

for i in Scores:
    if min>i:
        min=i


sum=sum-min-max
avg=sum/3

print("이 학생의 평균 점수는", avg , "입니다.")

