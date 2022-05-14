import turtle
win = turtle.Screen()
pen = turtle.Turtle()
win.setup(1200, 700)
win.title('Hello, World!')
def drawTripleTriangle(target, size, color):
    target.fillcolor(color)
    target.begin_fill()
    for i in range(3):
        target.forward(size)
        target.right(120)
        target.forward(size)
        target.right(120)
        target.forward(size)
    target.end_fill()

drawTripleTriangle(pen, 100, 'yellow')
drawTripleTriangle(pen, 50, 'black')
drawTripleTriangle(pen, 30, 'red')
