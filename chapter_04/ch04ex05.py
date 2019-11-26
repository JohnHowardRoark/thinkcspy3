# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 04 Exercise 05

""" tired of forgetting to update exercise number so moved it to a variable """
exercise = "Chapter 04: Exercise 05"

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

""" setup the canvas and turtle """
import turtle
wn = make_window("lightgreen", exercise)
tess = make_turtle("blue" , 2)

def draw_pattern(angle):
  tess.pendown()
  step = 5
  for i in range(51):
    tess.forward(step)
    tess.right(angle)
    tess.forward(step)
    tess.right(angle)
    step = step + 5

""" actual part that draws the pattern """
tess.right(180)

""" draw first spiral """
tess.penup()
tess.goto(-200,0)
draw_pattern(90)

""" draw second spiral """
tess.penup()
tess.goto(200,0)
draw_pattern(91)
 
wn.mainloop()