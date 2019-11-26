""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 16: Exercises 01 - 05
"""

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def print_point(pt):
        print("({0}, {1})".format(pt.x, pt.y))

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """ Exercise 01: Return the area of any instance. """
        return self.width * self.height

    def perimeter(self):
        """ Exercise 02: Return the perimeter of any instance. """
        return 2 * self.width + 2 * self.height

    def flip(self):
        """ Exercise 03: Swap the width and height of an instance. """
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, pt):
        """ Exercise 04: Method to test if a point falls within a rectangle. """
        return (pt.x >= self.corner.x and pt.x < (self.corner.x + self.width)) and (pt.y >= self.corner.y and pt.y < (self.corner.y + self.height))

    def corners(self):
        """ Return all 4 corners of a rectangle for collision detection. """
        pt1 = Point(self.corner.x, self.corner.y)
        pt2 = Point((self.corner.x + self.width), self.corner.y)
        pt3 = Point(self.corner.x, (self.corner.y + self.height))
        pt4 = Point((self.corner.x + self.width), (self.corner.y + self.height))
        return [pt1, pt2, pt3, pt4]
    
    def collides(self, targ):
        """ Exercise 05: Determine if two rectangles collide. This can also be done using self.area to determine which rectangle is larger, then only checking large.contains(points in small)
        """
        set_a = self.corners()
        set_b = targ.corners()
        for i in range(4):
            temp = set_b[i]
            if self.contains(temp):
                return True
        for i in range(4):
            temp = set_a[i]
            if targ.contains(temp):
                return True
        return False



def same_coordinates(p1, p2):
    """ Returns True if the points are the same. """
    return (p1.x == p2.x) and (p1.y == p2.y)


def test(did_pass):
    """  Print the result of a test.  """
    import sys
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        print("Test at line {0} ok." .format(linenum))
    else:
        print("Test at line {0} FAILED" .format(linenum))


def test_suite():
    """ Test suite for code in this module.
    """
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.area() == 50)
    test(r.perimeter() == 30)
    r = Rectangle(Point(100, 50), 10, 5)
    test(r.width == 10 and r.height == 5)
    r.flip()
    test(r.width == 5 and r.height == 10)
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))
    r = Rectangle(Point(0, 0), 10, 5)
    s = Rectangle(Point(4, 4), 10, 5)
    t = Rectangle(Point(0, 0), 1, 1)
    u = Rectangle(Point(2, 2), 2, 2)
    test(r.collides(s) == True)
    test(r.collides(t) == True)
    test(s.collides(t) == False)
    test(r.collides(u) == True)


test_suite()
