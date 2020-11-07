

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


def calc(no1, no2, oper):
    result = None
    if oper == '+':
        result = add(no1, no2)
    elif oper == '-':
        result = sub(no1, no2)
    elif oper == '*':
        result = mul(no1, no2)
    elif oper == '/':
        if no2 == 0:
            print("0으로 나눌수 없습니다.")
            return None
        else:
            result = div(no1, no2)
    elif oper == '%':
        result = rem(no1, no2)
    return result


while True :
    print("=========================")
    print("+ : 더하기\n- : 빼기\n* : 곱하기\n/ : 나누기\n% : 나머지구하기\nE : 나가기")
    print("=========================")
    oper = input("원하는 연산자를 입력하세요. ")
    operator = ['+', '-', '*', '/', '%','E']
    if oper=='E':
        print("종료를 선택하셨습니다. 프로그램을 종료합니다.")
        break
    elif oper not in operator:
        print("잘못된 연산자 입력입니다.")
        continue
    else:
        x = int(input("첫번째 숫자를 입력하세요. "))
        y = int(input("두번째 숫자를 입력하세요. "))
        result = calc(x, y, oper)
        if result != None:
            print("결과는", result, "입니다.")
