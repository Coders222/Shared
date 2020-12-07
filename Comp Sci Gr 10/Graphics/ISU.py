from graphics import *
from random import randint
import threading
import winsound
from playsound import playsound

win = GraphWin("window", 800, 600)
# main page

title = Text(Point(400, 200), "SHOOTER")
title.setSize(30)
title.draw(win)

playbutton = Rectangle(Point(200, 250), Point(375, 325))
playbutton.setFill("lightgreen")
playbutton.draw(win)

hexagon1 = Polygon(Point(200, 200), Point(235, 165), Point(270, 165), Point(305, 200), Point(305, 235), Point(270, 270),
                   Point(235, 270), Point(200, 235))  # copied from my previous graphics assignment

hexagon1.move(450, -75)  # had to move because of     ^^^^^
hexagon1.draw(win)

leftribbon = Polygon(Point(200, 235), Point(235, 270), Point(252, 400), Point(217, 365))
leftribbon.move(450, -75)
leftribbon.draw(win)

connector = Line(Point(270, 270), Point(252, 400))
connector.move(450, -75)
connector.draw(win)

rightribbon = Polygon(Point(305, 235), Point(270, 270), Point(252, 400), Point(288, 365))
rightribbon.move(450, -75)
rightribbon.draw(win)

highscore = Text(Point(703, 75), "HIGHSCORE")
highscore.setSize(15)
highscore.draw(win)

win.mainloop()




