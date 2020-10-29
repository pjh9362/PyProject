
user_in = int(input("입력 : "))

for i in range(user_in):
    print(' ' * (user_in-i),sep='',end='')
    print('*' * ((i+1) * 2 - 1), sep='')

print()

for i in range(user_in):
    for j in range(user_in-i):
        print(' ',end='')
    for j in range((i+1)*2 -1):
        print('*', end = '')
    print()

print()


for i in reversed(range(user_in)):
    for j in range(user_in-i):
        print(' ',end='')
    for j in range((i+1)*2 -1):
        print('*', end = '')
    print()

print()

for i in range(user_in):
    for j in range(i+1):
        print(' ',end='')
    for j in range((user_in-i)*2-1):
        print('*',end='')
    print()
        
