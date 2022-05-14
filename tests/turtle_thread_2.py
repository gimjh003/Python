'''
달리기 시합 프로그램
- 참가선수 : 거북이, 강아지, 고양이
'''

import turtle
import random
import threading
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

# 서로 동시에 달리게 하기 (threaded)

def turtle_run():
    while(Turtle.xcor()<=width/2-2*offset):
        Turtle.fd(random.randint(1,2))

def arrow_run():
    while(Arrow.xcor()<=width/2-2*offset):
        Arrow.fd(random.randint(2,8))

def circle_run():
    while(Circle.xcor()<=width/2-2*offset):
        Circle.fd(random.randint(1,7))

t1 = threading.Thread(target=turtle_run)
t2 = threading.Thread(target=arrow_run)
t3 = threading.Thread(target=circle_run)

t1.start(); t2.start(); t3.start()
win.mainloop()