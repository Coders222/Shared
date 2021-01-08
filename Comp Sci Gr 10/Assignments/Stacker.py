from graphics import *
from random import randint
import winsound
from playsound import playsound

gameScreen = GraphWin("window", 900, 900, autoflush=False)

blocks = [
"images/3block.gif",
"images/2block.gif",
"images/1block.gif"
]


# 75 x 75
hotkey = "Space"


base = Line(Point(188, 825), Point(713, 825))
border2 = Line(Point(188, 75), Point(188, 825))
border3 = Line(Point(713, 75), Point(713, 825))
base.draw(gameScreen)
border2.draw(gameScreen)
border3.draw(gameScreen)

verticals = []

for i in range(6):
    s = Line(Point(263 + 75 * i, 75), Point(263 + 75 * i, 825))
    verticals.append(s)
    s.draw(gameScreen)

horizontals = []

for i in range(9):
    s = Line(Point(188, 150 + 75 * i,), Point(713, 150 + 75 * i))
    horizontals.append(s)
    s.draw(gameScreen)

update()

playing = True

sizes = [112, 75, 37]

if playing:
    stacking = True
    while stacking:
        level = 0
        n = 0
        block = blocks[n]
        placing = True
        position = "left"
        size = sizes[n]
        while placing:
            if position == "left":
                position = 188 + size
            elif position == "right":
                position = 188 + 525 - size
            block = Image(Point(position, 788 - level * 75), block)
            block.draw(gameScreen)
            direction = 1
            while True:
                time.sleep(0.5 - 0.05 * level)
                block.move(75, 0)

                
            
