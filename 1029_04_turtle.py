import turtle as t

t.pensize(3)

t.shape('turtle')

for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(5):
    t.forward(100)
    t.right(360 / 5)


sh = int(input("몇 각형을 만드시겠습니까? : "))

for i in range(sh):
    t.forward(100)
    t.right(360/sh)
