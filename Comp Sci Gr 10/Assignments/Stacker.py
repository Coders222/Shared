from graphics import *
import threading
import winsound
import threading
import time

screen = "newTitle"
hotkey = "space"


while screen == "newTitle":
    titleScreen = GraphWin("Stacker", 600, 600, autoflush=False)
    title = Text(Point(300, 75), "S T A C K E R")
    title.draw(titleScreen)
    title.setSize(30)
    classic = Text(Point(300, 230), "Classic Mode")
    classic.draw(titleScreen)
    classic.setSize(20)
    classRect = Rectangle(Point(215, 220), Point(385, 240))
    classRect.draw(titleScreen)
    endless = Text(Point(300, 285), "Endless Mode")
    endless.draw(titleScreen)
    endless.setSize(20)
    endRect = Rectangle(Point(215, 275), Point(385, 295))
    endRect.draw(titleScreen)
    hotkeyTitle = Text(Point(300, 400), "Change HotKey")
    hotkeyTitle.draw(titleScreen)
    hotkeyTitle.setSize(17)
    keyRect = Rectangle(Point(215, 390), Point(385, 410))
    keyRect.draw(titleScreen)
    rules = Text(Point(300, 450), "Rules")
    rules.draw(titleScreen)
    rules.setSize(17)
    rulesRect = Rectangle(Point(265, 460), Point(335, 435))
    rulesRect.draw(titleScreen)
    screen = "title"

    cont = False
    while screen == "title":
        if cont:
            screen = "newTitle"
            break
        click = titleScreen.getMouse()
        if 385 >= click.getX() >= 215 and 240 >= click.getY() >= 220:  # if user clicks on classic
            titleScreen.close()
            gameScreen = GraphWin("Stacker", 900, 900, autoflush=False)

            screen = "classic"
            blocks = [
                "images/3block.gif",
                "images/2block.gif",
                "images/1block.gif"
            ]
            # 75 x 75

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
                s = Line(Point(188, 150 + 75 * i, ), Point(713, 150 + 75 * i))
                horizontals.append(s)
                s.draw(gameScreen)

            update()

            sizes = [112, 75, 37]  # midpoints of the blocks
            # hotkey = "space"  -  defined this at the top now
            level = 0
            n = 0
            block = blocks[n]
            starter = "left"
            position = 0
            size = sizes[n]
            placing = True
            stacking = True


            class classicMode(threading.Thread):
                def __init__(self):
                    threading.Thread.__init__(self)

                def run(self):
                    global position
                    global hotkey
                    global level
                    global size
                    global block
                    global stacking
                    global placing
                    global starter
                    global direction
                    while stacking:
                        if starter == "left":
                            position = 188 + size
                            direction = 1
                        elif starter == "right":
                            position = 188 + 525 - size
                            direction = -1

                        drawnblock = Image(Point(position, 788 - level * 75), block)
                        drawnblock.draw(gameScreen)

                        placing = True
                        update()
                        draw = True
                        while placing:
                            end = time.time() + 0.75 - 0.05 * level
                            while time.time() < end:  # while loop of 0.75 seconds
                                key = gameScreen.checkKey()
                                if key == hotkey:
                                    placing = False
                                    stacking = False
                                    draw = False
                                    if starter == "left":
                                        starter = "right"
                                    else:
                                        starter = "left"
                                    level += 1
                                    print(level)
                                    stacking = True
                            if draw:
                                drawnblock.move(75 * direction, 0)
                                position += 75 * direction
                                if position - (
                                        size + 1) <= 188 or position + size + 1 >= 713:  # + 1 because its 1 pixel off
                                    direction *= -1


            thread1 = classicMode()
            thread1.start()

        elif 385 >= click.getX() >= 215 and 295 >= click.getY() >= 275:  # if user wants to endless
            titleScreen.close()
            gameScreen = GraphWin("Stacker", 900, 900, autoflush=False)
            screen = "endless game"

        elif 385 >= click.getX() >= 215 and 410 >= click.getY() >= 390:  # if user clicks on hotkey
            titleScreen.close()
            hotkeyScreen = GraphWin("Hot Key Edit", 500, 500, autoflush=False)
            screen = "hotkey fix"

            currentHotkey = Text(Point(175, 150), "Current Hotkey: " + hotkey)
            currentHotkey.draw(hotkeyScreen)
            currentHotkey.setSize(17)

            changeKeyRect = Rectangle(Point(50, 250), Point(350, 300))
            changeKeyRect.draw(hotkeyScreen)
            changeKey = Text(Point(200, 275), "Click Here to Change Key")
            changeKey.draw(hotkeyScreen)

            confirmChangeRect = Rectangle(Point(50, 300), Point(350, 350))
            confirmChangeRect.draw(hotkeyScreen)
            confirmChange = Text(Point(200, 325), "Confirm Change and/or Exit")
            confirmChange.draw(hotkeyScreen)

            while screen == "hotkey fix":
                click = hotkeyScreen.getMouse()
                if 350 >= click.getX() >= 50 and 300 >= click.getY() >= 250:
                    changeKey.undraw()
                    selectKey = Text(Point(200, 275), "Select New Key")
                    selectKey.draw(hotkeyScreen)

                    confirmChangeRect.undraw()
                    confirmChange.undraw()

                    hotkey = hotkeyScreen.getKey()
                    currentHotkey.undraw()
                    currentHotkey = Text(Point(175, 150), "Current Hotkey: " + hotkey)
                    currentHotkey.draw(hotkeyScreen)
                    currentHotkey.setSize(17)

                    selectKey.undraw()
                    changeKey = Text(Point(200, 275), "Click Here to Change Key")
                    changeKey.draw(hotkeyScreen)
                    confirmChangeRect = Rectangle(Point(50, 300), Point(350, 350))
                    confirmChangeRect.draw(hotkeyScreen)
                    confirmChange = Text(Point(200, 325), "Confirm Change and/or Exit")
                    confirmChange.draw(hotkeyScreen)

                elif 350 >= click.getX() >= 50 and 350 >= click.getY() >= 300:
                    hotkeyScreen.close()
                    screen = "newTitle"
                    continue

        elif 335 >= click.getX() >= 265 and 460 >= click.getY() >= 435:  # if user clicks on rules
            titleScreen.close()
            rulesScreen = GraphWin("Rules", 500, 500, autoflush=False)
            skip = False
            while True:
                page1 = True
                page2 = False
                pg1 = []
                pg2 = []
                if skip:
                    cont = True
                    break
                if page1:
                    text1 = Text(Point(250, 50), "Classic Mode")
                    text1.setSize(25)
                    text1.draw(rulesScreen)
                    text1.setFill("blue")
                    pg1.append(text1)

                    rule1 = Text(Point(250, 100), "1. You will be given a starter 3x1 block to stack that is constantly moving")
                    rule1.setSize(10)
                    rule1.draw(rulesScreen)
                    pg1.append(rule1)
                    rule2 = Text(Point(250, 150),
                                 "2. The default hot key to stack is space, try to stack all blocks on your previous one")
                    pg1.append(rule2)
                    rule2.setSize(10)
                    rule2.draw(rulesScreen)
                    pg1.append(rule2)
                    rule3 = Text(Point(250, 200),
                                 "3. Everytime you misalign your new block with the previous block under it, \n"
                                 "you will lose the misaligned blocks, making a smaller base for you to stack on")
                    rule3.setSize(10)
                    rule3.draw(rulesScreen)
                    pg1.append(rule3)
                    rule4 = Text(Point(250, 250), "4. Speeds of the block constantly moving will increase after each level")
                    rule4.setSize(10)
                    rule4.draw(rulesScreen)
                    pg1.append(rule4)
                    rule5 = Text(Point(250, 300), "5. If you make it to level 4 with more than two blocks \n"
                                                  " remaining, you will be forced to lose one block")
                    rule5.setSize(10)
                    rule5.draw(rulesScreen)
                    pg1.append(rule5)
                    rule6 = Text(Point(250, 350), "6. If you make it to level 7 with more than one block remaining, \n "
                                                  "you will also be forced to lose one block")
                    rule6.setSize(10)
                    rule6.draw(rulesScreen)
                    pg1.append(rule6)
                    rule7 = Text(Point(250, 400), "7. Once you stack to the top, you win!")
                    rule7.setSize(10)
                    rule7.draw(rulesScreen)
                    pg1.append(rule7)

                    rule8 = Text(Point(250, 450), "TL;DR \n Time each placement of blocks on top of the \n"
                                                  "previous one, when you hit the top you win!")
                    rule8.setSize(13)
                    rule8.setFill("green")
                    rule8.draw(rulesScreen)
                    pg1.append(rule8)

                    exittext = Text(Point(475, 485), "Next")
                    exittext.setFill("red")
                    exittext.draw(rulesScreen)
                    pg1.append(exittext)

                    click = rulesScreen.getMouse()
                    while True:
                        if 460 <= click.getX() <= 490 and 480 <= click.getY() <= 490:
                            page2 = True
                            page1 = False
                            for i in pg1:
                                i.undraw()
                            break
                        click = rulesScreen.getMouse()

                if page2:

                    text1 = Text(Point(250, 50), "Endless Mode")
                    text1.setSize(25)
                    text1.draw(rulesScreen)
                    text1.setFill("blue")
                    pg2.append(text1)

                    rule1 = Text(Point(250, 100), "1. Same as classic mode but..")
                    rule1.setSize(10)
                    rule1.draw(rulesScreen)
                    pg2.append(rule1)
                    rule2 = Text(Point(250, 150),
                                 "2. You will be given power ups randomly to help you on your endless journey")
                    rule2.setSize(10)
                    rule2.draw(rulesScreen)
                    pg2.append(rule2)

                    exittext = Text(Point(475, 485), "Exit")
                    exittext.setFill("red")
                    exittext.draw(rulesScreen)
                    pg2.append(exittext)

                    backtext = Text(Point(25, 485), "Back")
                    backtext.setFill("red")
                    backtext.draw(rulesScreen)
                    pg2.append(backtext)

                    click = rulesScreen.getMouse()
                    while True:
                        if 460 <= click.getX() <= 490 and 480 <= click.getY() <= 490:  # quit
                            page2 = False
                            page1 = False
                            skip = True
                            rulesScreen.close()
                            break
                        elif 10 <= click.getX() <= 40 and 480 <= click.getY() <= 490:  # back
                            for i in pg2:
                                i.undraw()
                            page1 = True
                            page2 = False
                            break
                        click = rulesScreen.getMouse()




titleScreen.mainloop()