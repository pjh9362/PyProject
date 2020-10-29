'''
*****
 ****
  ***
   **
    *
'''

for i in range(5):
    for j in range(5):
        if i<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

for i in range(5):
    print(' '*i,sep='',end='')
    print('*'*(5-i), sep ='',end='')
    print()

print()

