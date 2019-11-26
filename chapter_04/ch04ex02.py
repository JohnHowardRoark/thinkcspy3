# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 04 Exercise 02

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

def draw_square(t, sides):
  """ non-fruitful function that draws a square """
  t.pendown()
  for i in range(4):
    t.forward(sides)
    t.left(90)
  t.penup()
  
""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", "Chapter 04: Exercise 02")
tess = make_turtle("hotpink" , 3)

""" actual part that draws the squares """
size_of_square = 20

for i in range(5):
  draw_square(tess, size_of_square)
  tess.forward(-10)
  tess.right(90)
  tess.forward(10)
  tess.left(90)
  size_of_square = size_of_square + 20

wn.mainloop()