from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

win = Screen()
win.setup(width=800, height=600)
win.bgcolor("black")
win.title("PONG")
win.tracer(0)

p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

win.update()
win.onkeypress(p1.up, "w")
win.onkeypress(p1.down, "s")
win.onkeypress(p2.up, "Up")
win.onkeypress(p2.down, "Down")
win.listen()

game = True
while game:
    win.update()
    time.sleep(ball.refresh)
    ball.move()
    if ball.xcor() >= 330 and p2.distance(ball) <= 60 or ball.xcor() <= -330 and p1.distance(ball) <= 60:
        ball.collision()
    if ball.xcor() >= 410:
        scoreboard.add_score_p1()
        ball.miss()
    elif ball.xcor() <= -410:
        scoreboard.add_score_p2()
        ball.miss()

win.exitonclick()