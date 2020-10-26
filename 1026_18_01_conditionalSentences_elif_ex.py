money = int(input("금액을 입력하세요 : "))

if money <= 10000 :
    juice = {"1":700, "2":600, "3":800}
    
    print("1-사이다(700원), 2-콜라(600원), 3-오렌지쥬스(800원)")
    drink = input("음료를 선택하세요 : ")

    if drink in juice:
        if money-juice[drink] >= 0:
            print("잔액은", money-juice[drink], "입니다")
        else:
            print("금액이 부족합니다.")
    else:
        print("잘못된 음료 선택입니다.")
    
else:
    print("최대 금액을 초과하였습니다.")



'''
juice = {"1" : 700 , "2" : 600, "3" : 800}

딕셔너리로 처리하면 더 간편하다.

'''
