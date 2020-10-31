import turtle as t

t.shape('turtle')
t.speed('fastest')
#t.pensize(2)

n = 60
for i in range(n):
    t.right(360 / n)
    t.circle(120)
