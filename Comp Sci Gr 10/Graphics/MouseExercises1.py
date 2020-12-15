from graphics import *
from random import randint
import threading

win = GraphWin("window", 800, 600, autoflush=False)

# 1


start = True
stem = None

while True:
    temp = win.getMouse()
    if start:
        stem = Point(0, 600)
        start = False
        continue
    line = Line(Point(stem.getX(), stem.getY()), Point(temp.getX(), temp.getY()))
    line.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
    line.draw(win)
    stem = Point(temp.getX(), temp.getY())
        
win.mainloop()


# 2

"""
class clear(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            key = win.getKey()
            if key == "c":
                blank = Rectangle(Point(0, 0), Point(800, 600))
                blank.setFill("white")
                blank.draw(win)


class drawing(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        temp = True
        prev = None
        while True:
            if temp:
                prev = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
                temp = False
                continue
            random1 = randint(0, 255)
            random2 = randint(0, 255)
            random3 = randint(0, 255)
            colour = color_rgb(random1, random2, random3)

            pos = win.getMouse()
            first = Point(pos.getX(), pos.getY())
            first.draw(win)
            pos2 = win.getMouse()
            rect = Rectangle(first, Point(pos2.getX(), pos2.getY()))
            first.undraw()
            rect.setFill(prev)
            rect.setOutline(colour)
            rect.setWidth(5)
            rect.draw(win)
            prev = colour


thread1 = drawing()
thread2 = clear()

thread1.start()
thread2.start()

win.mainloop()
"""

# 3

"""
circ = Circle(Point(250, 300), 200)
circ.setFill("yellow")
circ.draw(win)

eye1 = Oval(Point(190, 200), Point(210, 250))
eye1.setFill("black")
eye1.draw(win)

eye2 = Oval(Point(290, 200), Point(310, 250))
eye2.setFill("black")
eye2.draw(win)

angry = Rectangle(Point(600, 50), Point(775, 200))
angry.setFill("red")
angry.draw(win)
text1 = Text(angry.getCenter(), "ANGRY")
text1.setSize(25)
text1.draw(win)

sad = Rectangle(Point(600, 225), Point(775, 375))
sad.setFill("lightblue")
sad.draw(win)
text2 = Text(sad.getCenter(), "SAD")
text2.setSize(25)
text2.draw(win)

happy = Rectangle(Point(600, 400), Point(775, 550))
happy.setFill("lightgreen")
happy.draw(win)
text3 = Text(happy.getCenter(), "HAPPY")
text3.setSize(25)
text3.draw(win)

lip1 = Line(Point(202, 386), Point(150, 330))
lip1.setFill("black")
lip1.setWidth(10)
lip1.draw(win)

mainlip = Rectangle(Point(200, 380), Point(300, 390))
mainlip.setFill("black")
mainlip.draw(win)

lip2 = Line(Point(298, 385), Point(350, 330))
lip2.setWidth(10)
lip2.setFill("black")
lip2.draw(win)

# lip2 = 52, 55 diff

eyebrow1 = Line(Point(175, 150), Point(225, 200))
eyebrow2 = Line(Point(275, 200), Point(325, 150))
tear1 = Line(Point(1, 1), Point(2, 2))
tear2 = Line(Point(3, 3), Point(4, 4))

prev = "happy"


nothing = False

while True:
    click = win.getMouse()

    if nothing:
        nothing = False
        continue

    if 600 <= click.getX() <= 775 and 50 <= click.getY() <= 200:  # angry
        lip1.undraw()
        lip2.undraw()
        mainlip.undraw()
        eyebrow1.undraw()
        eyebrow2.undraw()
        tear1.undraw()
        tear2.undraw()

        lip1 = Line(Point(202, 383), Point(152, 433))
        lip1.setFill("black")
        lip1.setWidth(10)
        lip1.draw(win)

        mainlip = Rectangle(Point(200, 380), Point(300, 390))
        mainlip.setFill("black")
        mainlip.draw(win)

        lip2 = Line(Point(295, 382), Point(349, 440))
        lip2.setWidth(10)
        lip2.setFill("black")
        lip2.draw(win)

        eyebrow1 = Line(Point(175, 150), Point(225, 200))
        eyebrow1.setFill("black")
        eyebrow1.setWidth(10)
        eyebrow1.draw(win)

        eyebrow2 = Line(Point(275, 200), Point(325, 150))
        eyebrow2.setFill("black")
        eyebrow2.setWidth(10)
        eyebrow2.draw(win)

        circ.setFill("red")

    elif 600 <= click.getX() <= 775 and 225 <= click.getY() <= 375:  # sad
        lip1.undraw()
        lip2.undraw()
        mainlip.undraw()
        eyebrow1.undraw()
        eyebrow2.undraw()
        tear1.undraw()
        tear2.undraw()

        circ.setFill(color_rgb(17, 96, 145))

        lip1 = Line(Point(202, 383), Point(152, 433))
        lip1.setFill("black")
        lip1.setWidth(10)
        lip1.draw(win)

        mainlip = Rectangle(Point(200, 380), Point(300, 390))
        mainlip.setFill("black")
        mainlip.draw(win)

        lip2 = Line(Point(295, 382), Point(349, 440))
        lip2.setWidth(10)
        lip2.setFill("black")
        lip2.draw(win)

        # eye1 = Oval(Point(190, 200), Point(210, 250))
        # eye2 = Oval(Point(290, 200), Point(310, 250))

        x = 210

        while True:
            time.sleep(0.01)
            update()  # create lines instead?
            tear1.undraw()
            tear1 = Rectangle(Point(195, 210), Point(205, x))
            tear1.draw(win)

            tear2.undraw()
            tear2 = Rectangle(Point(295, 210), Point(305, x))
            tear2.draw(win)
            x += 1
            if x == 350:
                break

    elif 600 <= click.getX() <= 775 and 400 <= click.getY() <= 550:  # happy
        update()
        lip1.undraw()
        lip2.undraw()
        mainlip.undraw()
        eyebrow1.undraw()
        eyebrow2.undraw()
        tear1.undraw()
        tear2.undraw()

        lip1 = Line(Point(202, 386), Point(150, 330))
        lip1.setFill("black")
        lip1.setWidth(10)
        lip1.draw(win)

        mainlip = Rectangle(Point(200, 380), Point(300, 390))
        mainlip.setFill("black")
        mainlip.draw(win)

        lip2 = Line(Point(298, 385), Point(350, 330))
        lip2.setWidth(10)
        lip2.setFill("black")
        lip2.draw(win)
        circ.setFill("lightgreen")

    else:
        nothing = True
"""







