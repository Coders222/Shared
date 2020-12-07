from graphics import *

win = GraphWin("window", 800, 600)

rect = Rectangle(Point(200, 160), Point(350, 70))
rect.setOutline("red")
rect.setWidth("9")
rect.draw(win)

win.mainloop()