'''
달리기 시합 프로그램
- 참가선수 : 거북이, 강아지, 고양이
'''

import turtle
import random
win = turtle.Screen()
win.title("별무리경기장")
win.bgpic('')
width = 1200
height = 800
offset = 50
win.setup(width, height)

# win.addshape() or turtle.addshape()
# win.addshape()
# win.addshape()

Turtle = turtle.Turtle('turtle')
Arrow = turtle.Turtle('arrow')
Circle = turtle.Turtle('circle')

Turtle.penup()
Arrow.penup()
Circle.penup()

# 출발선으로 이동
Turtle.goto(-width/2+offset, -8/32*height)
Arrow.goto(-width/2+offset, -10/32*height)
Circle.goto(-width/2+offset, -12/32*height)

'''
# 달리기 시작
while(Turtle.xcor() < width/2-2*offset):
    Turtle.fd(random.randint(1, 2))
while(Arrow.xcor() < width/2-2*offset):
    Arrow.fd(random.randint(2, 8))
while(Circle.xcor() < width/2-2*offset):
    Circle.fd(random.randint(1, 7))
'''

# 서로 동시에 달리게 하기
while (Turtle.xcor() < width/2-2*offset) and (Arrow.xcor() < width/2-2*offset) and (Circle.xcor() < width/2-2*offset):
    Turtle.fd(random.randint(1, 2))
    Arrow.fd(random.randint(2, 8))
    Circle.fd(random.randint(1, 7))

