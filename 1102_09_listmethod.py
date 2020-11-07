#빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 자연수 1부터 10까지 추가
for i in range(1, 11):
    numbers.append(i)
print(numbers)

# numbers에서 홀수 제거
for index, value in enumerate(numbers):
    if value%2 == 1:
        #numbers.pop(index)
        numbers.remove(value)
print(numbers)

'''
i = len(numbers) - 1
while i>=0:
    if numbers[i] %2 == 1:
        del numbers[i]
    i-=1
'''


# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers에서 20을 찾아서 삭제
while 20 in numbers:
    numbers.remove(20)
print(numbers)

#numbers에서 4의 인덱스 찾기
print(numbers.index(4))

'''
result = []
for i in range(len(numbers)):
    if numbers[i]==4:
        result.append(i)
print(result)
'''

#numbers를 내림차순 정렬해서 출력
numbers.sort(reverse = True)
print(numbers.sort(reverse = True))
print(numbers)

'''
print에서의 실행과 차이
파이썬의 리스트는 .sort()메소드를 이용해서 정렬할 수 있다.
단 이 때의 정렬은 제자리 정렬로 .sort() 메소드는
리턴값이 없으며 리턴값이 없는 파이썬 함수가 늘 그러하듯 None을 리턴하기는 한다.
메소드를 호출한 원본 리스트의 내부 원소들이
순서를 비꾸게 된다.
'''

