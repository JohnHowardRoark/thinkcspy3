""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 04 Section 4.7 """

def make_window(colr, ttle):
  """ setup window with given background color and title """

  w = turtle.Screen()
  w.bgcolor(colr)
  w.title(ttle)
  return w

def make_turtle(color, size):
  """ sets up new turtle with given color and pensize """
  t = turtle.Turtle()
  t.color(color)
  t.pensize(size)
  t.shape("turtle")
  return t

import turtle
wn = make_window("lightgreen", "dancing")
tess = make_turtle("hotpink" , 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

tess.stamp()
alex.penup()
alex.forward(50)
alex.stamp()
dave.penup()
dave.forward(100)
dave.stamp()

wn.mainloop()