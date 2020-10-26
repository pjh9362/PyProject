operator = ["+", "-", "*", "/", "%"]

no1 = int(input("첫번째 숫자 : "))
no2 = int(input("두번째 숫자 : "))

user_oper = input("연산자 : ")

if user_oper in operator :
    if user_oper == "+":
        print("정답 : ", no1 + no2)
    elif user_oper == "-":
        print("정답 : ", no1 - no2)
    elif user_oper == "*":
        print("정답 : ", no1 * no2)
    elif user_oper == "/":
        if no2 == 0:
            print("잘못된 연산입니다.")
        else:
            print("정답 : ", no1/no2)
    elif user_oper == "%":
        if no2 == 0:
            print("잘못된 연산입니다.")
        else:
            print("정답 : ", no1%no2)
    else:
        pass
else:
    print("잘못된 연산자입니다.")

