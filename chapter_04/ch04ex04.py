# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 04 Exercise 04

""" tired of forgetting to update exercise number so moved it to a variable """
exercise = "Chapter 04: Exercise 04"

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

def draw_square(t, sz):
  """ non-fruitful function that draws a square """
  t.pendown()
  for i in range(4):
    t.forward(sz)
    t.left(90)
  t.penup()

def draw_shape():
  for i in range(4):
    draw_square(tess, 100)
    tess.left(90)
  
""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", exercise)
tess = make_turtle("blue" , 2)

""" actual part that draws the pattern """
tess.hideturtle()
for i in range(5):
  draw_shape()
  tess.left(18)

wn.mainloop()