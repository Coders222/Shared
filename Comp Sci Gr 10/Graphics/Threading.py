import threading
import time
from graphics import *
win = GraphWin("Threading example", 600, 800)


# Thread #1
class BallThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        cir = Circle(Point(50,400), 50)
        cir.setFill("red")
        cir.draw(win)

        while count != 20:
            cir.move(2, 0)
            time.sleep(0.05)


# Thread #2
class TimerThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        counter = Text(Point(300, 50), str(count))
        counter.draw(win)

        while count != 20:
            time.sleep(1)
            count += 1
            counter.setText(str(count))


count = 1

thread1 = BallThread()
thread2 = TimerThread()

thread1.start()
thread2.start()

win.mainloop()