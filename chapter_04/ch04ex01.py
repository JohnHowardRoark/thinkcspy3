# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 04 Exercise 01

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

def square(sides):
  """ non-fruitful function that draws a square """
  tess.pendown()
  for i in range(4):
    tess.forward(sides)
    tess.left(90)
  tess.penup()
  
""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", "Chapter 04: Exercise 01")
tess = make_turtle("hotpink" , 3)

""" actual part that draws the squares """
for i in range(5):
  square(20)
  tess.forward(40)

wn.mainloop()