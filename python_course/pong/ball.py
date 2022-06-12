from turtle import Turtle

SPEED_X = 10
SPEED_Y = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_x = SPEED_X
        self.speed_y = SPEED_Y
        self.refresh = 0.1
    def move(self):
        self.goto(self.xcor()+self.speed_x, self.ycor()+self.speed_y)
        if self.ycor() >= 285 or self.ycor() <= -280:
            self.bounce()
    def bounce(self):
        self.speed_y *= -1
    def collision(self):
        self.speed_x *= -1
        self.refresh *= 0.9
    def miss(self):
        self.collision()
        self.refresh = 0.1
        self.home()