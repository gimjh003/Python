import turtle
import sys

win = turtle.Screen()
t = turtle.Turtle('arrow')
step_size = 20

t.ondrag(t.goto)

def go_up():
    pos = t.pos()
    t.setpos(pos[0], pos[1]+step_size)

def go_right():
    pos = t.pos()
    t.setpos(pos[0]+step_size, pos[1])

def go_left():
    pos = t.pos()
    t.setpos(pos[0]-step_size, pos[1])

def go_down():
    pos = t.pos()
    t.setpos(pos[0], pos[1]-step_size)

def printpos():
    pos = t.pos()
    t.write(pos)

win.onkeypress(go_up, "Up")
win.onkeypress(go_right, "Right")
win.onkeypress(go_left, "Left")
win.onkeypress(go_down, "Down")
win.onkey(printpos, "p")
win.onkey(sys.exit, "e")
win.listen()
win.mainloop()