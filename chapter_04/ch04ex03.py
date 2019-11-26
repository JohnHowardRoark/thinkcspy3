# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 04 Exercise 03

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
  t.speed(0)
  return t

def draw_poly(t, n, sz):
  """ non-fruitful function that draws a regular polygon """
  t.pendown()
  for i in range(n):
    t.forward(sz)
    t.left(360 / n)
  t.penup()
  
""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", "Chapter 04: Exercise 03")
tess = make_turtle("hotpink" , 3)

""" actual part that draws the polygon """
draw_poly(tess, 8, 50)

wn.mainloop()