from turtle import Screen
from snake import Snake
from food import Food
from socreboard import Scoreboard
import time

win = Screen()
win.setup(width=600, height=600)
win.bgcolor("black")
win.title("My Snake Game")
win.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()

win.onkeypress(snake.up, "Up")
win.onkeypress(snake.down, "Down")
win.onkeypress(snake.left, "Left")
win.onkeypress(snake.right, "Right")
win.listen()

game = True
while game:
    win.update()
    time.sleep(0.1)
    snake.move()
    x = snake.head.xcor()
    y = snake.head.ycor()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            game = False
            scoreboard.game_over()
    if x >= 290 or x <= -290 or y >= 290 or y <= -290:
        snake.reset()
        scoreboard.reset()

win.exitonclick()