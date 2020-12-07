from graphics import *
from random import randint


win = GraphWin("window", 800, 600)

square = Rectangle(Point(10, 10), Point(50, 50))
square.draw(win)
circle = Circle(Point(80, 30), 20)
circle.draw(win)

drawingCircle = True
while True:
    random = randint(10, 100)
    location = win.getMouse()
    if 50 <= location.getX() <= 10 and 60 <= location.getY() <= 50:
        drawingCircle = False
    elif 10 <= location.getX() <= 50 and 10 <= location.getY() <= 50:
        drawingCircle = False
    elif 60 <= location.getX() <= 10 and 100 <= location.getY() <= 50:
        drawingCircle = True
    elif drawingCircle:
        circ = Circle(Point(location.getX(), location.getY()), random)
        circ.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        circ.draw(win)
    else:
        square = Rectangle(Point(location.getX() + random, location.getY() + random), Point(location.getX() - random, location.getY() - random))
        square.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        square.draw(win)



