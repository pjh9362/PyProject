import turtle as t

t.shape('turtle')
n=5
for i in range(n):
    t.forward(100)
    t.right((360/n)*2)
    t.forward(100)
    t.left(360/n)
