import turtle
win = turtle.Screen()
win.setup(1200, 700)
rainbow_size = 500
win.title('Hello, World!')
pen = turtle.Turtle()
pen.pensize(30)
pen.penup()
pen.speed(10)
def draw(n):
    pen.setheading(90)
    pen.setpos(rainbow_size/2-n*30, 0)
    pen.pendown()
    pen.circle(rainbow_size/2-n*30, 180)
    pen.penup()
for i in range(7):
    if i == 0:pen.pencolor('red')
    elif i == 1:pen.pencolor('orange')
    elif i == 2:pen.pencolor('yellow')
    elif i == 3:pen.pencolor('green')
    elif i == 4:pen.pencolor('blue')
    elif i == 5:pen.pencolor('blue4')
    elif i == 6:pen.pencolor('magenta')
    draw(i)

# 원을 그릴 때 주는 값은 반지름과 호에 해당하는 각도.
# 2로 나눈 이유는 반지름이기 때문이었구나.
# goto로 2로 나눈 값을 준 이유도 0,0을 중심으로 하기 위해서였어.