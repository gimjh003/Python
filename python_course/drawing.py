from turtle import Screen, Turtle

win = Screen()
t = Turtle()

def movefd():
    t.forward(5)

def movebk():
    t.forward(-5)

def rturn():
    t.rt(5)

def lturn():
    t.lt(5)

def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

win.listen()
win.onkeypress(movefd, "w")
win.onkeypress(movebk, "s")
win.onkeypress(lturn, "a")
win.onkeypress(rturn, "d")
win.onkeypress(clear, "c")
win.mainloop()