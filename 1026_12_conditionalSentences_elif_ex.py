x = int(input("입력값: "))

x -= 20

if x < 0:
    x=0
    print("출력값:",x)
elif 0 <= x <= 255:
    print("출력값:",x)
else:
    pass


'''
pixel = int(input("input:"))
if pixel - 20 > 0 :
    pixel = pixel - 20
else:
    pixel = 0
print("출력값 :", pixel)
'''

