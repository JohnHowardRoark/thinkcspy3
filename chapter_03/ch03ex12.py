# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 03 Exercise 11

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.pensize(5)
tess.speed(0)        # options are 0-10; 0 means no animation


for i in range(12):
  if i == 3:          # this stamps a mark vertically
    tess.stamp()
  tess.penup()
  tess.forward(100)
  tess.pendown()
  tess.forward(10)
  tess.penup()
  tess.forward(20)
  tess.stamp()
  tess.backward(130)  # or tess.forward(-130)
  tess.left(30)

tess.shape("blank")   # so now there is no horizontal tess left

wn.mainloop()
