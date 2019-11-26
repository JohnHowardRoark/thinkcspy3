# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 05 Exercise 11

turns = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

for i in range(len(turns)):
  tess.right(turns[i][0])
  tess.forward(turns[i][1])

wn.mainloop()