""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exerise 01: Draw a Koch snowflake (3 Koch fractals)
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


def koch(t, order, size):
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)


""" setup the canvas and turtle """
wn = make_window("lightgreen", "Chapter 18: Exercise 01")
t = make_turtle("blue" , 2)
t.penup()
t.goto(-200, 100)
t.pendown()

for i in range(3):
    koch(t, 2, 300)
    t.left(-120)

""" useful to ensure return to prompt after window is closed """
wn.mainloop()