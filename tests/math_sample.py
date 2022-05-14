import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2*self.radius*math.pi
    def get_circle_area(self):
        return self.radius**2*math.pi

circle = Circle(10)
print("원의 둘레 :", circle.get_circumference())
print('원의 넓이 :', circle.get_circle_area())