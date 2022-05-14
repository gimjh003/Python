# 단계별로 난이도가 상승한다.
# 시작 버튼, 다음 버튼, 종료 버튼이 존재한다.
# 거북이를 움직여(마우스 드래그 혹은 클릭) 탈출 경로를 그릴 수 있다.

import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.title('THE MAZE RUNNER')

stage = 0
window_width = 1200
window_height = 800
button_width = 150
button_height = 50
button_color = 'sky blue'
start_x = 400
start_y = 200
next_x = 400
next_y = 100
quit_x = 400
quit_y = 0

win.setup(window_width, window_height)
t.speed(500)

def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(width)
        t.right(90)
        t.fd(height)
        t.right(90)
    t.end_fill()

def draw_button(x, y, msg):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    draw_rectangle(button_width, button_height, button_color)
    t.goto(x+button_width/2, y-button_height)
    t.pencolor('white')
    t.write(msg, align="center", font=('Arial', 30))

def init():
    win.bgpic('')
    t.clear()
    draw_button(start_x, start_y, 'START')
    draw_button(next_x, next_y, 'NEXT')
    draw_button(quit_x, quit_y, 'QUIT')

def check_button(x, y):
    global stage
    if(x>=start_x and x<=start_x+button_width and y<=start_y and y>=start_y-button_height):
        stage=1
        init()
    elif(x>=next_x and x<=next_x+button_width and y<=next_y and y>=next_y-button_height):
        stage+=1
        init()
    elif(x>=quit_x and x<=quit_x+button_width and y<=quit_y and y>=quit_y-button_height):
        win.bye()
    else:
        t.goto(x, y)
        t.pendown()
        t.pencolor('black')
        print("클릭 확인됨")

init()
win.onclick(check_button)
t.ondrag(t.goto)

win.mainloop()