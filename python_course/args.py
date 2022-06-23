def add(*nums):
    print(sum(nums))

add(1,2,3,4,5,6,7,8,9,10)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
    
my_car = Car(make="Kim")

print(my_car.make, my_car.model)