from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90; DOWN = 270; LEFT = 180; RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for _ in range(3):
            self.segments.append(Turtle("square"))
            self.segments[_].color("white")
            self.segments[_].penup()
            self.segments[_].goto(0-20*_, 0)
    def move(self):
        """Snake move forward"""
        for segment in range(len(self.segments)-1, 0, -1):
            self.segments[segment].goto(self.segments[segment-1].pos())
        self.head.fd(MOVE_DISTANCE)
    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)