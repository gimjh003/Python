import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.setup(800, 800)
t.speed(100)
length = 100
traps = []
color = 'yellow'

def drawTrap(x, y, color):
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.right(90)
    t.end_fill()
    
with open('trap.txt', 'r') as file:
    while True:
        try:
            temp = file.readline().split(',')
            coordinate = [int(temp[0]), int(temp[1])]
        except:
            break
        else:
            traps.append(coordinate)

for trap in traps:
    drawTrap(trap[0], trap[1], color)
