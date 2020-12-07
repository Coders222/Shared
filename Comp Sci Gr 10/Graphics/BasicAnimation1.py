from Graphics.graphics import *
import winsound
# 1

"""
win = GraphWin("Window", 600, 800)

circle = Circle(Point(300, 400), 50)
circle.draw(win)
circle.setFill("red")
direction = 1
y = 400

while True:
    time.sleep(0.1)
    circle.move(0, 10 * direction)
    y += 10 * direction
    if y >= 750 or y <= 50:
        direction *= -1
"""

# 2

"""
win = GraphWin("window", 800, 800)

house = Image(Point(400, 400), "images/house.gif")
house.draw(win)

pikachu = Image(Point(100,700), "images/pikachu.gif")
pikachu.draw(win)

jigglypuff = Image(Point(700, 700), "images/jigglypuff.gif")
jigglypuff.draw(win)


direction1 = 1
direction2 = 1
pos1 = 700
pos2 = 700

while True:
    time.sleep(0.01)
    jigglypuff.move(-10 * direction1, -10 * direction1)
    pikachu.move(5 * direction2, -5 * direction2)
    pos1 += -10 * direction1
    pos2 += -5 * direction2
    if pos1 <= 100 or pos1 >= 700:
        direction1 *= -1
    if pos2 <= 100 or pos2 >= 700:
        direction2 *= -1
"""

# 3


win = GraphWin("window", 800, 400)

girl = Image(Point(100, 200), "images/girl.gif")
girl.draw(win)
boy = Image(Point(700, 200), "images/boy.gif")
boy.draw(win)

pos = 170
direction = 1


plane = None

while True:
    if direction == -1:
        plane = planeLeft = Image(Point(625, 150), "images/planeLeft.gif")
    else:
        plane = planeRight = Image(Point(175, 150), "images/planeRight.gif")
    plane.draw(win)
    winsound.PlaySound(None, winsound.SND_PURGE)
    key = win.getKey()
    if key == "space":
        winsound.PlaySound("sounds/planeSound.wav", winsound.SND_ASYNC)
        while 170 < pos + (5 * direction) < 630:
            time.sleep(0.01)
            plane.move(5 * direction, 0)
            pos += 5 * direction
        direction *= -1
        plane.undraw()

        







    
    












