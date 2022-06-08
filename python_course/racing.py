from turtle import Screen, Turtle
import random

win = Screen()
win.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
for idx, turtle in enumerate(turtles):
    turtles[turtle].goto(-230, -75+idx*30)
user_bet = win.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ").lower()
goal=False
while not goal:
    for turtle in turtles:
        turtles[turtle].fd(random.randint(1, 10))
        if turtles[turtle].xcor() >= 230:
            goal = True
            print(f"Win : {turtle}")
            if user_bet == turtle:
                print("You got it, here's 100 million dollars.")
            else:
                print("That's poor. I'll take your life.")