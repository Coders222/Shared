from graphics import *

win = GraphWin("Window", 600, 800)

# 1.
# a)
"""
rect = Rectangle(Point(60,130), Point(100,90))
rect.draw(win)


line1 = Line(Point(60,130), Point(100,90))
line2 = Line(Point(60,90), Point(100,130))
line1.setFill("green")
line2.setFill("green")

line2.draw(win)
line1.draw(win)

win.mainloop()
"""

# b)
"""
line1 = Line(Point(160,230), Point(160, 180))
line1.setFill("green")
line2 = Line(Point(160,230), Point(210,230))
line2.setFill("green")

line1.draw(win)
line2.draw(win)

topline = Line(Point(160, 230), Point(170, 185))
topline.setFill("green")

topline.draw(win)
middleline = Line(Point(160,230), Point(200, 190))
middleline.setFill("green")

middleline.draw(win)
bottomline = Line(Point(160,230), Point(205, 210))
bottomline.setFill("green")

bottomline.draw(win)
"""


# c)
"""
rect1 = Rectangle(Point(260,330), Point(300,290))
rect1.setOutline("green")
rect1.draw(win)


rect2 = Rectangle(Point(260,330), Point(315,275))
rect2.setOutline("green")
rect2.draw(win)

rect3 = Rectangle(Point(260,330), Point(330,260))
rect3.setOutline("green")
rect3.draw(win)

rect4 = Rectangle(Point(260,330), Point(345,245))
rect4.setOutline("green")
rect4.draw(win)
"""

                  
# 2
"""
rect1 = Rectangle(Point(150,200), Point(200, 250))
rect1.setFill("blue")
rect1.draw(win)

rect2 = Rectangle(Point(250,200), Point(300, 250))
rect2.setFill("yellow")
rect2.draw(win)

line1 = Line(Point(200,250), Point(250,200))
line1.setFill("green")
line1.draw(win)

line1 = Line(Point(200,200), Point(250,250))
line1.setFill("green")
line1.draw(win)
"""

#3

"""
oval = Oval(Point(180,20), Point(220,80))
oval.setFill("cyan")
oval.draw(win)
"""

#4

"""
circle1 = Circle(Point(240,160), 25)
circle1.setFill("green")
circle1.setOutline("black")
circle1.setWidth(5)
circle1.draw(win)


circle2 = Circle(Point(240,110), 25)
circle2.setFill("grey")
circle2.setOutline("blue")
circle2.setWidth(5)
circle2.draw(win)
"""

#5

"""
rect = Rectangle(Point(90, 40), Point(160, 110))
rect.setFill("magenta")
rect.draw(win)

circle = Circle(Point(125,75), 35)
circle.setFill("green")
circle.setOutline("black")
circle.setWidth(3)
circle.draw(win)
"""

#6

"""
win.setBackground("black")


oval1 = Oval(Point(30,30), Point(50, 70))
oval2 = Oval(Point(80,30), Point(100, 70))
oval3 = Oval(Point(55,80), Point(75, 120))

oval1.setFill("lightblue")
oval2.setFill("white")
oval3.setFill("red")
oval1.draw(win)
oval2.draw(win)
oval3.draw(win)

line1 = Line(Point(40, 50), Point(90,50))
line1.setFill("grey")
line2 = Line(Point(40, 50), Point(65,100))
line2.setFill("grey")
line3 = Line(Point(84, 66), Point(74,90))
line3.setFill("grey")

line1.draw(win)
line2.draw(win)
line3.draw(win)
"""

#7
"""
hexagon1 = Polygon(Point(200, 200), Point(250,150), Point(300,150), Point(350, 200), Point(350,250), Point(300, 300),
                   Point(250, 300), Point(200,250))
hexagon1.setFill("light blue")
hexagon1.draw(win)

text1 = Text(Point(275,225), "O")
text1.draw(win)



hexagon2 = Polygon(Point(400, 400), Point(450,350), Point(500,350), Point(550, 400), Point(550,450), Point(500, 500),
                   Point(450, 500), Point(400,450))
hexagon2.setFill("orange")

hexagon2.draw(win)



text2 = Text(Point(475,425), "C")
text2.draw(win)
"""

#8

"""
image = Image(Point(300,400), "images\halloween.gif")
image.draw(win)


square1 = Rectangle(Point(100,400), Point(120,575))
square1.setOutline("grey")
square1.draw(win)

bigsquare = Rectangle(Point(120,400), Point(450, 575))
bigsquare.setFill("lightblue")
bigsquare.draw(win)

square2 = Rectangle(Point(450,575), Point(470,400))
square2.setOutline("grey")
square2.draw(win)

line1 = Line(Point(100,400), Point(120, 370))
line1.setOutline("lightblue")
line1.draw(win)

line2 = Line(Point(470,400), Point(480, 360))
line2.setOutline("lightblue")
line2.draw(win)


text1 = Text(Point(285, 488), "Stay safe during Halloween!")
text1.draw(win)

hatbase = Rectangle(Point(120,250), Point(450, 220))
hatbase.draw(win)
hatbase.setFill("grey")

hattop = Polygon(Point(180, 220), Point(390, 220), Point(285, 100), Point(180, 220))
hattop.draw(win)
hattop.setFill(color_rgb(255, 7, 0))
"""

win.mainloop()












