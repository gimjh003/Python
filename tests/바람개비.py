import turtle
win = turtle.Screen()
t = turtle.Turtle()
size = 100
t.pensize(20)

def drawGiyeok(x, y, angle, color):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.pencolor(color)
    t.forward(size)
    t.right(90)
    t.forward(size)

def drawPinwheel(x, y, color):
    for i in range(0, 360, 45):
        drawGiyeok(x, y, i, color)

drawPinwheel(-200, 200, 'alice blue')
drawPinwheel(0, 0, 'lavender')
drawPinwheel(200, 200, 'lavender blush')
drawPinwheel(-200, -200, 'misty rose')
drawPinwheel(200, -200, 'navajo white')