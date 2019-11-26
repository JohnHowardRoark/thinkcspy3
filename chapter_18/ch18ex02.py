""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exercise 02 a, b, c
"""

import turtle
import math


def make_window(colr, ttle):
    """ setup the window with given background color and title """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    w.setup(width=1800, height=600)
    return w


def make_turtle(color, size):
    """ setup the turtle with given color and pensize """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.hideturtle()      # do not show turtle
    t.speed(0)     # 0 - 10 scale, 0 is fastest
    return t


def koch(t, order, ang, size):
    """
       Draw a Cesaro fractal of a given size and tear angle.
       Leave the turtle facing the same direction.
    """
    turn = 90 - (ang/2)
    size = size - (size * math.sin(math.radians(ang/2)))
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for i in [turn, -2*turn, turn, 0]:
           koch(t, order-1, ang, size/2)
           t.right(i)


""" Set locations and starting order. User input for angle. """
# angle = int(input("Angle: \n"))
angle = 10
locations = [(-800, 150), (-400, 150), (0, 150), (400,150)]
order = 0

""" Setup the canvas and turtle. """
wn = make_window("lightgreen", "Chapter 18: Exercise 02")
tess = make_turtle("blue" , 2)

""" Draw 4 fractals spaced horizontally using the angle given. """
for r in range(4):
    tess.penup()
    tess.goto(locations[r])
    tess.pendown()
    for i in range(4):
        koch(tess, order, angle, 300)
        tess.right(90)
    order += 1

""" This ensures return to prompt after window is closed. """
wn.mainloop()