""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 15: Exercises 01 - 04
"""


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def reflect_x(self):
        """ Exercise 02: Add a method to reflect a point about the x-axis.
        """
        return (self.x, -self.y)

    def slope_from_origin(self):
        """ Exercise 03: Return the slope of a line joining the origin to the point.
        """
        return (self.y / self.x)

    def get_line_to(self, target):
        """ Exercise 04: Method that computes the slope and intercept from the point to a given point. Fails if both points are the same (div 0).
        """
        m = (target.y - self.y) / (target.x - self.x)
        b = self.y - (m * self.x)
        return (m, b)


def distance(p, q):
    """ Exercise 01: Rewrite distance function so it takes 2 Points as parameters.
    """
    dx = q.x - p.x
    dy = q.y - p.y
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result


def test(did_pass):
    """  Print the result of a test.  """
    import sys
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED" .format(linenum))
    print(msg)


def test_suite():
    """ Test suite for code in this module.
    """
    test(distance(Point(0, 0), Point(3, 4)) == 5)
    test(Point(3, 5).reflect_x() == (3, -5))
    test(Point(4, 10).slope_from_origin() == 2.5)
    test(Point(4, 11).get_line_to(Point(6, 15)))


test_suite()