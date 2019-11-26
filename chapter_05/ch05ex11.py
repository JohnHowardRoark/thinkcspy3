""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 11
"""

def find_hypot(a, b):
    c = ((a ** 2) + (b ** 2)) ** 0.5
    return c

def is_right_angled(a, b, c):
    x = find_hypot(a, b)
    if abs(x - c) < .000001:
        return True
    else:
        return False



print(is_right_angled(3, 4, 5))     # should return True
print(is_right_angled(3, 4, 6))     # should return False