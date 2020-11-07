
# module -> 미리 만들어 놓은 무언가
# function - 특정 용도의 코드를 한곳에 모아 놓은 것
# print, input 등 - 파이썬에서 미리 만들어 둔 함수
'''
함수의 장점 - 
코드의 용도를 구분할 수 있다.
코드를 재사용할 수 있다.
실수를 줄일 수 있다.
'''

#형식
'''
def functionName(parameters):
    function
'''

def hello():
    print("Hello, world!")

hello()

for i in range(10):
    hello()
    
# def을 먼저 해주어야만 사용가능 (다른 언어들과 다름)


'''
def functionName(parameter1, parameter2, ...):
    code
'''
#넣는 값을 인수 argument
def add(a,b):
    print(a+b)
    

add(10, 20)
print(add(10,20))

def add(a,b):
    return a+b

#return 을 명시하지 않으면 default -> None

x = add(10,20)
y = add(5, 7)

print(x, y)
print(add(10,20), add(5,7))


# exercise 1

def triple_multiply(a,b,c):
    return a*b*c
'''
x = int(input())
y = int(input())
z = int(input())
result = triple_multiply(x,y,z)
print(result)
'''

# return 값이 꼭 하나가 아니어도 된다. 여러개의 값을 return 가능 tuple로 return


def add_sub(a,b):
    return a+b, a-b

x,y = add_sub(10, 20)
print(x)
print(y)

t= add_sub(50, 5)
print(t, type(t))

#unpacking
x,y = t
print(x, y)


#operator

def operator(a,b):
    return a+b, a-b, a*b, a/b

x, y = map(int, input().split())
r1, r2, r3, r4 = operator(x, y)
print('+ result : %d  - result : %d  * result : %d  / result : %f ' %(r1,r2,r3,r4) )

print('+ result : %d  - result : %d  * result : %d  / result : %f ' % operator(x,y) )


# 함수의 호출 과정 알아보기
def mul(a, b):
    c = a * b
    return c

def add(a,b):
    c = a + b
    print(c)
    d = mul(a,b)
    print(d)

x = 10
y = 20
add(x, y)
