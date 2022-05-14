import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.colormode(255)
width = 40
data = [120, 140, 160, 300, 80, 90, 250, 130]
t.speed(300)
t.pencolor('red')
t.up()
t.goto(-200, -200)
t.down()

def draw_bar(value):
    t.fillcolor(value%255, 0, 0)
    t.begin_fill()
    t.lt(90)
    t.fd(value)
    t.rt(90)
    t.fd(width)
    t.rt(90)
    t.fd(value)
    t.left(90)
    t.end_fill()

for i in data:
    draw_bar(i)