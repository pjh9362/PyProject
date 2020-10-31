
n = int(input("순환할 숫자를 입력하시용 : "))

for i in range(n):
    for j in range(i, i+n):
        print((j%n)+1,end=' ')
    print()
        
        
num = 0
i = 0
num = int(input())
while i<num:
    j = 0
    while j<num:
        print((i+j)%num + 1, end = ' ')
        j+=1
    print()
    i+=1
    
