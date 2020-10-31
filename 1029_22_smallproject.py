
age = 0
while True:
    age=int(input())
    if age>=7:
        break
    else:
        print("나이를 다시 입력하세요")

change = 9000

if age>=19:
    change-=1250
elif age>=13:
    change-=1050
else:
    change-=650

print("잔액 :", change)
