
a, b = map(int, input().split())

if a>=1 and a<=20 and b>=10 and b<=30 and a<b:
    l = []
    for i in range(a,b+1):
        l.append(2**i)
    del l[1]
    del l[-2]
    print(l)
else:
    print("잘못된 수 입력입니다.")
    
'''
a,b = 0,0
print(a,b)

while not(1<=a<=20 and 10<=b<=30 and a<b):
    a, b = map(int, input().split())
    
print(a,b)
'''

data1, data2 = map(int, input().split())

if(data1 < 1 or data1>20):
    print("1st data range error")
elif(data2<10 or data2>30):
    print("2nd data range error")
else:
    mylist = [2**i for i in range(data1, data2+1)]
    del mylist[1]
    del mylist[len(mylist)-2]
    print(mylist)
