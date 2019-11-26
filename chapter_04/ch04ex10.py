""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 04 Exercise 10 """

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Chapter 04 Exercise 10")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(0)

for x in range(5):
  for i in range(5):
    tess.forward(100)
    tess.right(144)
  tess.penup()
  tess.forward(350)
  tess.right(144)
  tess.pendown()


wn.mainloop()