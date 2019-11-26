""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 07 """

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Chapter 05 Exercise 07")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)
tess.speed(0)

xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs:              
    draw_bar(tess, v)

wn.mainloop()
