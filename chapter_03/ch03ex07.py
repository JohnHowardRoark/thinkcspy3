# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 03 Exercise 07

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

end_angle = 0

for i in range(len(turns)):
  tess.forward(100)
  tess.right(turns[i])
  end_angle = end_angle + turns[i]

wn.mainloop()

print(end_angle)