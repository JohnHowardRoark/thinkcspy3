""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 04 Exercise 08 """

def area_of_circle(r):
  """ this uses a finite float value for pi """
  return 3.1415926535 * r  ** 2

print(area_of_circle(10))

def area_of_circle_accurate(r):
  """ importing math for its pi value """
  import math
  return math.pi * r ** 2

print(area_of_circle_accurate(10))
