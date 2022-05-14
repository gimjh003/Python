import turtle
win = turtle.Screen()
ball = turtle.Turtle('circle')
ball.penup()

xvel = 3 # x축 방향 속력
yvel = 3 # y축 방향 속력
start_x = -300 # 시작점 x좌표
start_y = 200 # 시작점 y좌표
floor = -300 # 바닥 y좌표
overall_time = 200
restitution_coefficient = 0.8 # 반발계수

ball.goto(start_x, start_y) # 시작 위치로 이동
ball.down()
time = 0 
while time < overall_time: # 시뮬레이션 시간동안 반복
    if ball.ycor() < floor and yvel < 0: # 바닥을 만났고, 내려가는 속력이라면
        yvel = yvel * -restitution_coefficient # y축 방향 속력 반전
    ball.setx(ball.xcor()+xvel) # x축 방향 속력 위치에 반영
    ball.sety(ball.ycor()+yvel) # y축 방향 속력 위치에 반영
    yvel -= 1 # (중력에 의해) y축 방향 속력 감소 (y좌표겂이 감소하는거임)
    time = time+1 # 시간 증가