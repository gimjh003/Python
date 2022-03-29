class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()

class FlyableUnit2(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship2 = FlyableUnit2()