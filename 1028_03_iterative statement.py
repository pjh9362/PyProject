
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

print()

'''
*****
*****
*****
*****
*****
'''

for i in range(5):
    for j in range(5):
        print("*",end='')
    print()

print()

'''
*******
*******
*******
'''

for i in range(3):
    for j in range(7):
        print("*",end='')
    print()


print()


'''
*
**
***
****
*****
'''


for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()

print()

# python 에서만 가능한 특징을 이용

for i in range(5):
    print('*'* (i+1) ,sep='')
    
print()

for i in range(5):
    for j in range(5):
        if j > i:
            break
        print("*",end='')
    print()

print()

'''
*    
 *   
  *  
   * 
    *
'''


for i in range(5):
    for j in range(5):
        if i==j:
            print('*',end='')
        else:
            print(' ', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if i==j:
            print('*',end='')
        else:
            print(' ', end='')
    print()
    
print()



print()

'''
   *
  ***
 *****
*******
'''

for i in range(4):
    for j in range(4-1-i):
        print(' ',end='')
    for j in range((i+1)*2-1):
        print('*',end='')
    print()

print()

for i in range(1,5):
    for j in range(5-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()

print()

for i in range(4):
    print(' '*(4-i),sep='',end='')
    print('*'*((i+1)*2-1),sep='')
        
print()

rows = 4
for i in range(1, rows+1):
    print(' '*(rows-i) + '*'*(2*i-1))

print()

