# 다음과 같이 동작하는 프로그램을 작성해보자.
# 거북이를 왼쪽 클릭시 거북이를 빨간색으로 변경한다.
# 왼쪽 버튼 릴리즈 시, 거북이를 원래대로 검은색으로 변경한다.
# 거북이를 오른쪽 클릭 시, 거북이를 파란색으로 변경한다.
# 오른쪽 버튼 릴리즈 시, 거북이를 원래대로 검은색으로 변경한다.
# 거북이를 드래그 시, 거북이를 이동시키며 선을 긋는다.

import turtle
win = turtle.Screen()
t = turtle.Turtle('turtle')

def click_left(x, y):
    t.color('red')

def click_right(x, y):
    t.color('blue')

def release(x, y):
    t.color('black')

def drag(x, y):
    t.goto(x, y)

t.onclick(click_left, 1)
t.onclick(click_right, 3)
t.onrelease(release, 1)
t.onrelease(release, 3)

t.ondrag(drag)