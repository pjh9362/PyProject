import turtle as t

t.pensize(3)

# 삼각형 만들기
t.penup()
t.goto(-200, -50)
t.pendown()
t.circle(40, steps=3)
t.circle(40)

#사각형 만들기
t.penup()
t.goto(-100, -50)
t.pendown()
t.circle(40, steps=4)
t.circle(40)

# 오각형 만들기
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(40, steps = 5)
t.circle(40)

# 육각형 만들기
t.penup()
t.goto(100, -50)
t.pendown()
t.circle(40, steps = 6)
t.circle(40)

#원 만들기
t.penup()
t.goto(200, -50)
t.pendown()
t.circle(40)
