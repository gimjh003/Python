import turtle

# 윈도우 창 크기 변수
window_width = 1200
window_height = 800

# 버튼 크기 변수
button_width = 150
button_height = 50

# 펜 기본 색상 변수
text_color = 'WHITE'
default_pen_color = 'BLACK'

# 색상 조정 버튼 관련 변수
button_color_startx = window_width/2-170
button_color_starty = 200
button_color_red = 'RED'
button_color_green = 'GREEN'
button_color_blue = 'BLUE'

# 굵기 조정 버튼 관련 변수
thick_default = 5
button_thick_startx = window_width/2-170
button_thick_starty = 0
sample_len = 140
thick_lev1 = 5
thick_lev2 = 10
thick_lev3 = 15

# 옵션 버튼 관련 변수
button_opt_startx = window_width/2-170
button_opt_starty = -150
button_color_opt = 'BLACK'

# 기본 환경 설정
win = turtle.Screen()
t = turtle.Turtle()
win.setup(window_width, window_height)
win.title('My first paint')
win.addshape('pen_mk3.gif')
t.shape('pen_mk3.gif')
t.turtlesize(40, 40)
t.speed(1000)

# 버튼 형태 그리기
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(width)
        t.right(90)
        t.fd(height)
        t.right(90)
    t.end_fill()

# 색상 조정 버튼 그리기
def draw_color_opt(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    draw_rectangle(width, height, color)
    t.pencolor(text_color)
    t.goto(x+button_width/2, y-button_height)
    t.write(color, align='center', font=('Arial', 30))
    t.pencolor(default_pen_color)

# 굵기 조정 버튼 그리기
def draw_thick_opt(x, y, thick, len):
    t.penup()
    t.goto(x, y)
    t.pensize(thick)
    t.pencolor(default_pen_color)
    t.pendown()
    t.fd(len)
    t.penup()
    t.pensize(thick_default)

# 옵션 버튼 그리기
def draw_opt(x, y, width, height, color, opt):
    t.penup()
    t.goto(x, y)
    draw_rectangle(width, height, color)
    t.pencolor(text_color)
    t.goto(x+button_width/2, y-button_height)
    t.write(opt, align="center", font=('Arial', 30))
    t.pencolor(default_pen_color)

# 초기화 클릭 오류 방지
init_process = 0

# 초기화 설정
def init():
    global init_process
    init_process = 1
    t.clear()
    t.setheading(0)

    # 색상 조정 버튼 그리기
    draw_color_opt(button_color_startx, button_color_starty-button_height*0, button_width, button_height, button_color_red)
    draw_color_opt(button_color_startx, button_color_starty-button_height*1, button_width, button_height, button_color_green)
    draw_color_opt(button_color_startx, button_color_starty-button_height*2, button_width, button_height, button_color_blue)

    # 굵기 조정 버튼 그리기
    draw_thick_opt(button_thick_startx, button_thick_starty-button_height*0, thick_lev1, sample_len)
    draw_thick_opt(button_thick_startx, button_thick_starty-button_height*1, thick_lev2, sample_len)
    draw_thick_opt(button_thick_startx, button_thick_starty-button_height*2, thick_lev3, sample_len)

    # 옵션 버튼 그리기
    draw_opt(button_opt_startx, button_opt_starty-button_height*0, button_width, button_height, button_color_opt, "ERASE")
    draw_opt(button_opt_startx, button_opt_starty-button_height*1, button_width, button_height, button_color_opt, "QUIT")

    # 초기화 종료
    init_process = 0
    t.penup()

# 버튼 확인 함수
def check_button(x, y):

    # 클릭 영역 - 색상
    if (x>=button_color_startx) and (x<=button_color_startx+button_width):
        if (y<=button_color_starty-button_height*0) and (y>button_color_starty-button_height*1):
            t.pencolor(button_color_red)
        elif (y<=button_color_starty-button_height*1) and (y>button_color_starty-button_height*2):
            t.pencolor(button_color_green)
        elif (y<=button_color_starty-button_height*2) and (y>button_color_starty-button_height*3):
            t.pencolor(button_color_blue)

    # 클릭 영역 - 굵기
    if (x>=button_thick_startx) and (x<=button_thick_startx+button_width):
        if (y<=button_thick_starty-button_height*0+10) and (y>button_thick_starty-button_height*1+10):
            t.pensize(thick_lev1)
        elif (y<=button_thick_starty-button_height*1+10) and (y>button_thick_starty-button_height*2+10):
            t.pensize(thick_lev2)
        elif (y<=button_thick_starty-button_height*2+10) and (y>button_thick_starty-button_height*3+10):
            t.pensize(thick_lev3)

    # 클릭 영역 - 옵션
    if (x>=button_opt_startx) and (x<=button_opt_startx+button_width):
        if (y<=button_opt_starty) and (y>button_opt_starty-button_height*1):
            init()
        elif (y<=button_opt_starty) and (y>button_opt_starty-button_height*2):
            win.bye()
            
    # 클릭 영역 - 기본
    else:
        t.penup()

# 마우스 따라다니기
def pen_follow(event):
    if init_process == 0:
        x, y = event.x, event.y
        t.goto(x-win.window_width()/2, -y+win.window_height()/2)

canvas = turtle.getcanvas()
canvas.bind("<Motion>", pen_follow)

# 그리기 시작
def pen_draw_start(x, y):
        t.pendown()
        print(t.pos())

# 그리기 종료
def pen_draw_end(x, y):
        t.penup()
        t.goto(x, y)
        print(t.pos())

# 초기화 후 클릭 이벤트 동작 설정
init()
win.onclick(check_button)
t.ondrag(pen_draw_start)
t.onrelease(pen_draw_end)

# 입력 기다리기
win.mainloop()