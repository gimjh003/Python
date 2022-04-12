from itertools import count
import random
import turtle
import threading

time = 0
count = 0
win = turtle.Screen()
win.setup(700, 700)
t = turtle.Turtle('turtle')
timer = turtle.Turtle('arrow')
timer.hideturtle()
timer.penup()
timer.goto(100, 300)
t.penup()

def show(x, y):
    global count
    count += 1
    t.hideturtle()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.showturtle()

def check_minute():
    global time
    time += 1
    timer.clear()
    timer.write(f"경과 시간 : {time}초 잡은 개수 : {count}")
    thread = threading.Timer(1, check_minute)
    if time<60:
        thread.start()

thread = threading.Thread(target=check_minute)
thread.start()

t.onclick(show)

win.mainloop()
