import random

def make_question():
    no1 = random.randint(-99,99)
    no2 = random.randint(-99,99)
    oper = None
    temp = random.randint(1,3)
    
    if temp == 1:
        oper = '+'
    elif temp == 2:
        oper = '-'
    else:
        oper = '*'
        
    return str(no1) + oper + str(no2)


count = 0

for i in range(5):
    question = make_question()
    print("문제", i+1, " : ",question, "= ", end = " ")
    user_result = int(input())
    result = eval(question)
    if user_result == result:
        count+=1
        print("정답입니다.")
    else:
        print("오답입니다.")

print("총 5문제 중 ", count, "개 맞추셨습니다.")
