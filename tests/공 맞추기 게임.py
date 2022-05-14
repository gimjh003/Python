# 발사 각도 - fire_angle
# 발사 속력 - vel
# x축 방향 속력, y축 방향 속력 -> vx, vy
# 현재 위치와 각도 -> x, y, angle
# 발사 각도 조절 함수 -> turnLeft(), turnRight()
# 발사 함수 -> fire()

import math # 삼각함수 이용을 위해 math 모듈 불러오기
import turtle
win = turtle.Screen()
player = turtle.Turtle('turtle')

fire_angle = 5 # 발사 각도 조절 크기
vel = 80 # 발사 속력

def turn_left():
    player.left(fire_angle)

def turn_right():
    player.right(fire_angle)

def fire():
    x = player.xcor() # 현재 x좌표 읽기
    y = player.ycor() # 현재 y좌표 읽기
    angle = player.heading() # 현재 발사 각도 읽기
    # 현재 발사 각도를 radian 단위로 변환하고, y축 속력 계산
    vy = vel*math.cos(math.radians(angle))
    # 현재 발사 각도를 radian 단위로 변환하고, x축 속력 계산
    vx = vel*math.sin(math.radians(angle))
    while player.xcor() >= -300: # 바닥(y좌표가 0)을 만나기 전까지는
        vy -= 10 # y축 속력은 중력가속도에 의해 감소
        x = x+vx # x축 속력(vx)값을 이용해서 x축 좌표 업데이트
        y = y+vy # y축 속력(vy)값을 이용해서 y축 좌표 업데이트
        player.goto(x, y) # 업데이트된 좌표로 이동

win.onkeypress(turn_left, 'Left')
win.onkeypress(turn_right, 'Right')
win.onkeypress(fire, "space")

# x, y좌표축 그리기
player.goto(300, 0)
player.goto(-300, 0)
player.goto(-300, 300)
player.goto(-300, 0)

win.listen()
win.mainloop()