""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 04 Exercise 09 """

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Chapter 04 Exercise 09")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(0)

for x in range(5):
  tess.forward(100)
  tess.right(144)


wn.mainloop()