import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

win = Screen()
win.setup(width=600, height=600)
win.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

win.listen()
win.onkey(turtle.move, "Up")
game=True
while game:
    time.sleep(0.1)
    win.update()
    car_manager.add_car()
    if turtle.ycor() >= 300:
        scoreboard.increase_score()
        car_manager.clear()
        turtle.next()
    car_manager.move()
    if car_manager.collision(turtle):
        scoreboard.gameover()
        game = False

win.exitonclick()