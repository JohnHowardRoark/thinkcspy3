""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 12
"""

def find_hypot(a, b):
    c = ((a ** 2) + (b ** 2)) ** 0.5
    return c

def is_right_angled(a, b, c):
    x1 = abs(find_hypot(a, b) - c)
    x2 = abs(find_hypot(a, c) - b)
    x3 = abs(find_hypot(b, c) - a)
    if x1 < .000001 or x2 < .000001 or x3 < .000001:
        return True
    else:
        return False



print(is_right_angled(3, 4, 5))     # should return True
print(is_right_angled(5, 3, 4))     # should return True
print(is_right_angled(3, 5, 4))     # should return True
print(is_right_angled(3, 6, 4))     # should return False