import winsound
from graphics import *
import threading

win = GraphWin("window", 800, 800, autoflush=False)

# winsound.PlaySound("sounds/uzi.wav", winsound.SND_ASYNC | winsound.SND_LOOP)  # <-- really loud for some reason

boypos = [400, 400]
pikapos = [100, 100]
jigpos = [700, 700]

direction = 1


class Character(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        boy = Image(Point(400, 400), "images/boy.gif")
        boy.draw(win)
        global boypos
        global running
        global direction
        while running:
            update()
            key = win.checkKey()
            if key == "Right":
                boy.move(5, 0)
                boypos[0] += 5
            elif key == "Left":
                boy.move(-5, 0)
                boypos[0] -= 5
            elif key == "Up":
                boy.move(0, -5)
                boypos[1] -= 5
            elif key == "Down":
                boy.move(0, 5)
                boypos[1] += 5
            if boypos[1] + 115 >= jigpos[1] - 60 and boypos[0] == jigpos[0]:  # 115 and 60 are half the
                winsound.PlaySound("sounds/bruh.wav", winsound.SND_ASYNC)  # height of the images
                running = False  # ^^^ it will cause program to stop when the bottom of the boy hits or goes over top of
            elif boypos[1] - 115 <= pikapos[1] + 65 and boypos[0] == pikapos[0]:  # pikachu
                winsound.PlaySound("sounds/bruh.wav", winsound.SND_ASYNC)  # just made the x coords match bcuz im too
                running = False  # lazy to do the same (hit the boundary and stops the program)


class NPC(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global pikapos
        global jigpos
        global running
        global direction
        pikachu = Image(Point(100, 100), "images/pikachu.gif")
        pikachu.draw(win)
        jigglypuff = Image(Point(700, 700), "images/jigglypuff.gif")
        jigglypuff.draw(win)
        update()
        while running:
            update()
            time.sleep(0.01)
            pikachu.move(5 * direction, 0)
            pikapos[0] += 5 * direction
            jigglypuff.move(-5 * direction, 0)
            jigpos[0] -= 5 * direction
            if pikapos[0] >= 700 or pikapos[0] <= 100:
                direction *= -1


running = True

thread1 = Character()
thread2 = NPC()
thread1.start()
thread2.start()


win.mainloop()

