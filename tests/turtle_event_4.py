# 아래와 같이 이벤트를 좀 더 확장하여 키보드로 거북이를 움직이는 프로그램을 작성해보자.

# 화살표 키(Right, Left, Up, Down)를 이용한다.
# P나 p키를 누르면 현재 거북이 위치(좌표)를 화면에 출력한다.

import turtle
win = turtle.Screen()
t = turtle.Turtle()

step_size = 30 # 거북이 움직임 기본 단위

def go_up():
    pos = t.pos()
    t.setpos(pos[0], pos[1]+step_size)

def go_down():
    pos = t.pos()
    t.setpos(pos[0], pos[1]-step_size)

def go_right():
    pos = t.pos()
    t.setpos(pos[0]+step_size, pos[1])

def go_left():
    pos = t.pos()
    t.setpos(pos[0]-step_size, pos[1])

def write_pos():
    pos = t.pos()
    t.write(pos)

t.penup()

win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_right, "Right")
win.onkeypress(go_left, "Left")
win.onkey(write_pos, 'p')

win.listen()