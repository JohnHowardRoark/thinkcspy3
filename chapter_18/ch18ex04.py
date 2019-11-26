""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exercise 04: Sierpinski triangles with color change
"""

import turtle


def make_window(colr, ttle):
    """ setup the window with given background color and title """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    w.setup(width=800, height=600)
    return w


def make_turtle(x, y, spd):
    """ etup the turtle with given color and starting location. """
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(2)
    t.hideturtle()
    t.penup()
    t.speed(0)      # 0 - 10 scale, 0 is fastest
    t.goto(x, y)
    t.pendown()
    t.speed(spd)
    return t


def sier(t, order, size, colorChangeDepth=-1):
    """ Draw Sierpinski triangles of a given size and order>
    """
    global colors

    if order == 0:
        for x in range(3):
            t.forward(size)
            t.left(120)
    else:
        for i in range(3):
            if colorChangeDepth == 0:
                t.color(colors[0])
            sier(t, order-1, size/2, colorChangeDepth-1)
            t.penup()
            t.forward(size)
            t.left(120)
            t.pendown()
        colors.append(colors[0]), colors.pop(0) # list rotation


""" Ask user for order and depth of color change"""
order = int(input("Order:\n"))
depth = int(input("Color change depth:\n"))

""" Setup the canvas and turtle. Locate the turtle in the view area."""
wn = make_window("lightgreen", "Chapter 18: Exercise 04")
t = make_turtle(-200, -150, 0) # start location x, and y, speed
colors = ["red", "blue", "magenta"] # color rotation


""" Draw the triangles """
sier(t, order, 400, depth)

""" This ensures return to prompt after window is closed. """
wn.mainloop()

