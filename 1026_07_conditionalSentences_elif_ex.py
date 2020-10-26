money = int(input("금액을 입력하세요 : "))

drink = int(input("음료를 선택하세요.\n1.콜라 (600원) 2.사이다 (700원) 3.환타 (800원) :"))

if drink == 1 :
    print('잔액:', money - 600)
elif drink == 2:
    print('잔액:', money - 700)
elif drink == 3:
    print('잔액:', money - 800)
else :
    print('없는 음료입니다.')
