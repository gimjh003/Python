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
    else:
        try:
            scores = []
            scores.append(count)
            with open('leaderboard.txt', 'r', encoding="utf8") as file:
                file.readline()
                leaderboard = file.readlines()
                for score in leaderboard:
                    point = int(score.split()[1])
                    scores.append(point)
                scores.sort()
                scores.reverse()
            with open('leaderboard.txt', 'w', encoding="utf8") as file:
                file.write("최고 기록\n")
                for i in range(len(scores)):
                    file.write(f"{i+1}. {scores[i]} 마리 / 1분\n")
                    
        except Exception:
            with open('leaderboard.txt', 'w', encoding="utf8") as file:
                file.write(f"최고 기록\n1. {count} 마리 / 1분\n")
thread = threading.Thread(target=check_minute)
thread.start()

t.onclick(show)

win.mainloop()
