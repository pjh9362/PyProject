'''
# 함수 바깥쪽에 있는 지역 변수 a,b를 사용하여 a*x+b를 계산하는 함수 mul_add를 만든 뒤에 함수 mul_add자체를 반환

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b        # 함수 바깥쪽에 있는 지역 변수 a,b를 사용하여 계산
    return mul_add              # mul_add 함수를 반환

c = calc()

print(c(1), c(2), c(3), c(4), c(5))
'''

'''

# lambda로 클로저 만들기

def calc():
    a = 3
    b = 5
    return lambda x : a * x + b         # 람다 표현식을 반환

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 람다는 이름이 없는 익명 함수를 뜻하고, 클로저는 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수를 뜻함

'''


# 클로저의 지역 변수 변경하기

# 클로저의 지역 변수를 변경하고 싶다면 nonlocal을 사용하면 됨

def calc():
    a = 3
    b = 5
    total = 0                           # total이 mul_add 외부에 있으므로 값이 변한 상태에서 유지 됨

    def mul_add(x):
        nonlocal total                  # total = 0 새로 생성시 mul_add 내부에서 매번 초기화 됨 -> 결과 : 8 11 14
#        total = 0
        total = total + a * x + b       
        print(total)

    return mul_add

c = calc()

c(1)
c(2)
#c(3)

print()

b = calc()
b(3)
print(b(3))
