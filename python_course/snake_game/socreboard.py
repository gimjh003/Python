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
        with open("python_course/snake_game/data.txt") as f:
            self.high_score = int(f.readline())
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("python_course/snake_game/data.txt", "w") as f:
                f.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()