""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 23: Exercise 02: Define a new turtle with special features
"""

import random
import turtle
from turtle import Turtle, Screen

turtle.setup(600,400)   # set total window size


class TurtleGTX(Turtle):

    # rng = random.Random()

    def __init__(self):
        Turtle.__init__(self)
        self.color("red")
        self.pensize(2)
        self.shape("turtle")
        self.speed(0)
        self.odometer = 0
        self.flat_tyre = False
        # self.tyre_range = rng.randrange(100, 1001)

    def forward(self, dist):
        self.odometer += abs(dist)
        self._go(dist)

    def jump(self, dist):
        # self.odometer += abs(dist)
        self.penup()
        self.forward(dist)
        self.pendown()


def make_window():
    """ setup and return the window """
    w = turtle.Screen()
    w.bgcolor("lightgreen")
    w.title("Insert title here")
    return w


def make_turtle():
    """ setup and return the turtle """
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(2)        # 1 - 10 (I think)
    t.hideturtle()      # do not show turtle
    t.showturtle()      # show turtle
    t.shape("turtle")   # turtle shape (turtle, circle, etc.)
    t.speed(0)          # 0 - 10 scale, 0 is fastest
    return t


""" make the canvas and turtle """
wn = make_window()
tess = TurtleGTX()
tess.forward(50)
tess.jump(50)
print(tess.odometer)
a = turtle.textinput("Turtle command:", "What next?")

""" turtle movement """
# tess.penup()            # lift the pen so no line is drawn
# tess.pendown()          # lower the pen so a line is drawn
# tess.begin_fill()       # denotes the beginning of a fill area
# tess.end_fill()         # denotes end of fill area
# tess.goto(100, 100)     # goto x and y cooridnates
# tess.forward(100)       # go forward 100
# tess.backward(100)      # go backward 100
# tess.forward(-100)      # go backward 100
# tess.left(90)
# tess.right(90)
# tess.left(-90)
# tess.circle(40, 180)    # make a circle

""" useful to ensure return to prompt after window is closed """
wn.mainloop()
