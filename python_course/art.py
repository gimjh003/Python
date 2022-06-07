import turtle as t
import random
import colorgram

colors = colorgram.extract("sample.jpg", 30)
colors = [(x.rgb.r, x.rgb.g, x.rgb.b) for x in colors]

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

directions = [0, 90, 180, 270]
turtle = t.Turtle()
win = t.Screen()
t.colormode(255)
turtle.shape("circle")
turtle.speed("fastest")
turtle.penup()

for _ in range(10):
    turtle.goto(-200, -200+_*50)
    for __ in range(10):
        turtle.color(random.choice(colors))
        turtle.fd(50)
        turtle.stamp()

# def draw_spirograph(gap):
#     for _ in range(int(360/gap)):
#         turtle.color(generate_random_color())
#         turtle.circle(100)
#         turtle.rt(gap)

# turtle.pensize(10)
# for _ in range(200):
#     turtle.color(generate_random_color())
#     turtle.rt(random.choice(directions))
#     turtle.fd(30)

# turtle.color("red")
# for _ in range(3, 11):
#     for __ in range(_):
#         turtle.fd(100)
#         turtle.rt(360/_)

# draw_spirograph(5)

win.mainloop()