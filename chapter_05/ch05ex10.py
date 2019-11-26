""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 10
"""

def find_hypot(a, b):
    c = ((a ** 2) + (b ** 2)) ** 0.5
    return c

print(find_hypot(3, 4))