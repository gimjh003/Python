from turtle import Turtle

FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.p1_score = 0
        self.p2_score = 0
        self.goto(0, 200)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"{self.p1_score}  |  {self.p2_score}", align="center", font=FONT)
    def add_score_p1(self):
        self.p1_score += 1
        self.update_score()
    def add_score_p2(self):
        self.p2_score += 1
        self.update_score()