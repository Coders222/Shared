from graphics import *
from random import randint

win = GraphWin("window", 800, 600)

rect = Rectangle(Point(200, 200), Point(500, 500))
rect.draw(win)


x = 0
while True:
    time.sleep(2)
    rect.undraw()
    rect = Rectangle(Point(200, 200), Point(500 - x, 500 - x))
    x += 10
    rect.draw(win)



