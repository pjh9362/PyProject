'''
x = list(map(int, input().split()))


sum = 0
for i in x:
    sum+=i


    
avg = sum/len(x)

if avg>=80:
    print("합격")
else:
    print("불합격")
'''


kor = int(input())
eng = int(input())
mat = int(input())
sci = int(input())

if (0<=kor<=100 and 0<=eng<=100 and 0<=mat<=100 and 0<=sci<=100):
    tot = (kor+eng+mat+sci) / 4
    if tot>=80:
        print("합격")
    else:
        ptint("불합격")
else:
    print("잘못된 점수")
