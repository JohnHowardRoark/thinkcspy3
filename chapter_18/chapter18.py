""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exercise 02
"""

import turtle


def make_window(colr, ttle):
    """ setup the window with given background color and title """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(color, size):
    """ setup the turtle with given color and pensize """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.hideturtle()      # do not show turtle
    t.speed(0)     # 0 - 10 scale, 0 is fastest
    return t


""" setup the canvas and turtle """
wn = make_window("lightgreen", "Turtle")
tess = make_turtle("blue" , 2)
tess.penup()
tess.forward(-250)
tess.pendown()

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [85, -170, 85, 0]:
           koch(t, order-1, size/3)
           t.right(angle)


koch(tess, 3, 600)
""" useful to ensure return to prompt after window is closed """
wn.mainloop()