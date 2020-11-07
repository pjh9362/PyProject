

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

while True :
    print("=========================")
    print("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.나머지구하기\n6.나가기")
    print("=========================")
    oper = int(input("원하는 연산자를 입력하세요. "))
    if oper==6:
        print("종료를 선택하셨습니다. 프로그램을 종료합니다.")
        break
    elif not(1<=oper<=6):
        print("잘못된 연산자 입력입니다.")
        continue
    else:
        x = int(input("첫번째 숫자를 입력하세요. "))
        y = int(input("두번째 숫자를 입력하세요. "))
        result = 0
        if oper == 1:
            result = add(x,y)
        elif oper == 2:
            result = sub(x,y)
        elif oper == 3:
            result = mul(x,y)
        elif oper == 4:
            if y == 0:
                print("0으로 나눌수 없습니다.")
                continue
            else:
                result = div(x,y)
        elif oper == 5:
            result = rem(x,y)
        
        print("결과는", result, "입니다.")
