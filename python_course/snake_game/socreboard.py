from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()