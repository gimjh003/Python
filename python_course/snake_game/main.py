from turtle import Screen, Turtle
from snake import Snake
import time

win = Screen()
win.setup(width=600, height=600)
win.bgcolor("black")
win.title("My Snake Game")
win.tracer(0)

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

win.exitonclick()