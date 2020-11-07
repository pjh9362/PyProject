# '{인덱스}'.format(값)

print('Hello, {0}'.format('world!'))

print('Hello, {0}'.format(100))

s = 'Hello, {0}'.format('world!')
print(len(s))


print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))

print('Hello, {0} {2} {1} {1} {1} {1} {1}'.format('Python', 'Script', 3.6))

print('{0} {0} {1} {1}'.format('Python', 'Script'))

print('Hello, {} {} {}'.format('Python', 'Script', 3.6))

print("Hello, {language} {version}".format(language = "Python", version = 3.6))


# 3.6 이상 지원
# f문자열 포매팅

language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')


#{인덱스:<길이}'.format(값)

print('{0:<10}'.format('python')) # 0: 0 번 인덱스를 // 10: 10만큼 길이 확보하여 // < :왼쪽 정렬

# {인덱스:>길이}'.format(값)

print('{0:>10}'.format('python'))

print('{:>10}'.format('python'))

print('"{0:<10} {2:>10}{1:<10}"'.format('python', 'abc', 123))

#숫자 개수 맞추기
# '%0개수d' % 숫자
# '{index:0개수d'}'.format(숫자)

# '%0개수.자릿수f' % 숫자                       '%0길이.자릿수f' % 숫자 - 이게 더 정확한 표현 같음
# '{index:0개수.자릿수f'}.format(숫자)

print("********************")

print('%03d' % 1)
print('{0:03d}'.format(35))

print('%08.2f' % 3.6)
print('{0:018.2f}'.format(150.37))

#채우기와 정렬을 조합
# '{ 인덱스:[채우기][정렬][길이][.자릿수][자료형]}'

print('{0:0<10}'.format(15))            # 길이 10 왼쪽으로 정렬하고 남는 공간은 0

print('{0:0>10}'.format(15))            # 길이 10 오른쪽으로 정렬 남는 공간은 0으로

print('{0:0>10.2f}'.format(15))         # 길이 10 소숫점 아래 2자리로 남는 공간은 0



print('{0: >10}'.format(15))            # 공백으로 빈 칸을 채워 오른쪽 정렬

print('{0:>10}'.format(15))             # 채우기 문자를 생락하면 자동으로 공백 들어감

print('{0:x>10}'.format(15))            # 문자 x로 공백을 채움


