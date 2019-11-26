""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 06
"""

import sys

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    result = ((dx ** 2) + (dy ** 2)) ** 0.5
    return result


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED" .format(linenum))
    print(msg)


def test_suite():
    """ Test suite for code in this module.
    """
    test(distance(0, 0, 3, 4) == 5)


test_suite()
    