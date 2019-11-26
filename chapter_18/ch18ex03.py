""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exercise 03: Sierpinski triangles
"""

import turtle


def make_window(colr, ttle):
    """ setup the window with given background color and title """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    w.setup(width=800, height=600)
    return w


def make_turtle(color, size):
    """ setup the turtle with given color and pensize """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.hideturtle()      # do not show turtle
    t.speed(0)     # 0 - 10 scale, 0 is fastest
    return t


def sier(t, order, size):
    """ Draw Sierpinski triangles of a given size and order>
    """
    if order > -1:
        for i in range(3):
            t.forward(size)
            t.left(120)
            sier(t, order-1, size/2)
    else:
        pass


""" Ask user for order """
order = int(input("Order:\n"))

""" Setup the canvas and turtle. Relocate the turtle in the view area."""
wn = make_window("lightgreen", "Chapter 18: Exercise 03")
t = make_turtle("blue" , 2)
t.penup()
t.goto(-200,-150)
t.pendown()

""" Draw the triangles """
sier(t, order, 400)

""" This ensures return to prompt after window is closed. """
wn.mainloop()