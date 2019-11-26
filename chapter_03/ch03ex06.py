# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 03 Exercise 06

big = int(input("How big?"))

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

def draw_poly(sides, size):
  angle = 360 / sides
  for i in range(sides):
    tess.forward(size)
    tess.left(angle)

draw_list = [3, 4, 6, 8]

for i in range(len(draw_list)):
  x = draw_list[i]
  draw_poly(x, big)

wn.mainloop()