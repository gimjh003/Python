PI = 3.141592

def number_input():
    output = input("숫자 입력 > ")
    return float(output)

def get_circumference(radius):
    return 2*radius*PI

def get_circle_area(radius):
    return radius**2*PI