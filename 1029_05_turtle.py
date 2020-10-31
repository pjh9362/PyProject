import turtle as t

t.pensize(2)

n=6

t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.end_fill()
