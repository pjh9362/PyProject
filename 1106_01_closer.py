'''
x = 10

def foo():
    x = 20
    print(x)

foo()
print(x)

'''
'''
x = 10              # 전역 변수
def foo():
    global x        # 전역 변수 x를 사용하겠다고 설정
    x = 20          # x는 전역 변수
    print(x)        # 전역 변수 출력

print(x)
foo()
print(x)            # 전역 변수 출력

'''

# 전역 변수 x가 없는 상태

def foo():
    global x        # x를 전역 변수로 만듦
    x = 20          # x는 전역 변수
    print(x)        # 전역 변수 출력

foo()
print(x)            # 전역 변수 출력

# 함수 안에서 함수 만들기
'''
def function1():
    code
    def function2():
        code
'''

def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()

print_hello()

# print_message()       NameError: name 'print_message' is not defined
