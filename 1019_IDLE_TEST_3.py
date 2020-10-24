import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange", "white"]
t=turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length<700:
    t.forward(length)
    t.pencolor(colors[length % 7])
    t.right(89)
    length += 5
