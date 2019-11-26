""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 07 Exercise 12
"""

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
    t.hideturtle()
    return t


def make_house(i):
    """ This function draws a single house. The first element of the input list is used as the offset so houses do not overlap.  The second element of the list is used as the starting point for that house.
    """
    offset = i[0]
    start = i[1]
    new_start = start[0] + offset[0], start[1] + offset[1]
    del i[0:2]
    tess.speed(0)
    tess.penup()
    tess.goto(new_start)
    tess.pendown()
    tess.speed(2)
    for n in range(len(i)):
        tess.goto(i[n][0] + offset[0], i[n][1] + offset[1])


""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", "Chapter 07: Exercises 12 & 13")
tess = make_turtle("blue" , 2)

""" all points used to draw houses """
bl = (0 ,0)       # bottom left
br = (100, 0)     # bottom right
tl = (0, 100)     # top left
tr = (100, 100)   # top right
tc = (50, 150)    # top center (peak of house)
ct = (50, 50)     # center of square
ls = (-50, 50)    # point to left of house
rs = (150, 50)    # point to right of house

""" format for house points is:
    (offset, starting point, point1, point2, etc)
"""

""" Exercise 12 """
make_house([(-500, 0), bl, tr, br, bl, tl, tr, tc, tl, br])

""" Exercise 13, house # 1 """
make_house([(-300, 0), tl, tl, bl, br, tr, tl, tc, tr])

""" Exercise 13, house # 2 """
make_house([(-100, 0), tr, br, bl, tl, tr, tc, tl, br])

""" Exercise 13, house # 5 """
make_house([(150, 0), bl, ls, tc, rs, br, bl, tl, tr, br])

""" Exercise 13, house # 6 """
make_house([(400, 0), tl, br, bl, tl, tr, br, rs, tc, ls, bl, tr])

wn.mainloop()