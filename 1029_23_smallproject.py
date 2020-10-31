
x = int(input())

x+=20
if x>255:
    x=255
    print(x)
elif x<0:
    print("0보다 작은 값")
else:
    print(x)
