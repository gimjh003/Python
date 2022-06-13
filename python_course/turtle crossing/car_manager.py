from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.rt(180)
        self.reset()
    def move(self, spd):
        self.fd(spd)
    def reset(self):
        self.goto(random.randint(330, 800), random.randint(-250, 250))
    def clear(self):
        self.spd += 10
        self.reset()
    def collision(self, turtle):
        if turtle.ycor() >= self.ycor()-10 and turtle.ycor() <= self.ycor()+10:
            if self.distance(turtle) <= 20:
                return True

class CarManager:
    def __init__(self):
        self.cars = []
        self.spd = STARTING_MOVE_DISTANCE
    def move(self):
        for car in self.cars:
            car.move(self.spd)
            if car.xcor() <= -300:
                car.reset()
    def collision(self, turtle):
        for car in self.cars:
            if car.collision(turtle):
                return True
    def clear(self):
        self.spd += MOVE_INCREMENT
        for car in self.cars:
            car.hideturtle()
        self.cars = []
    def add_car(self):
        if random.randint(1, 6) == 1:
            self.cars.append(Car())