""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 06
"""

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    result = ((dx ** 2) + (dy ** 2)) ** 0.5
    return result
    

assert distance(0, 0, 3, 4) == 5, "Test failed."

print(distance(0, 0, 3, 4))



    