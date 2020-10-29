
for i in range(1,101):
    if i%3==0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

print()

for i in range(1,101):
    if i%15==0:
        # 3과 5의 최소공배수이므로 15로 나눴을때 나머지가 0인 값은 3, 5의 공배수
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

print()

# or 연산자의 단락 평가를 이용하여 출력. 0 이외 숫자는 True, 빈문자열을 제외한 문자열은 True
# 문자열에 True를 곱하면 문자열이 그대로 나온다. (True는 1로, False는 0으로 계산)

for i in range(1,101):
    print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)


