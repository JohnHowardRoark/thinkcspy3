""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 21: Exercises 01 - 05
"""

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
       """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
       """
       totalsecs = hrs*3600 + mins*60 + secs
       self.hours = totalsecs // 3600        # Split in h, m, s
       leftoversecs = totalsecs % 3600
       self.minutes = leftoversecs // 60
       self.seconds = leftoversecs % 60

    def __str__(self):
        """ Make print pretty. """
        return "({0}:{1}:{2})".format(self.hours, self.minutes, self.seconds)

    def __eq__(self, other):
        """ Overload equivalence operator for use in testing """
        return self.to_seconds() == other.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def __gt__(self, other):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > other.to_seconds()

    def to_seconds(self):
        """ Return the number of seconds represented by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def between(self, t1, t2):
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()

    def increment(self, seconds):
        return self.__init__(0, 0, self.to_seconds() + seconds)


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)

    def __mul__(self, other):
        """ Returns dot product. """
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        """ Returns scalar multiplication. """
        return Point(other * self.x,  other * self.y)


def test(did_pass):
    """  Print the result of a test.  """
    import sys
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        print("Test at line {0} ok." .format(linenum))
    else:
        print("Test at line {0} FAILED" .format(linenum))


def multadd (x, y, z):
    return x * y + z


def test_suite():
    """ Test suite for code in this module.
    """
    t1 = MyTime(2, 20, 0)
    t2 = MyTime(2, 20, 0)
    t3 = MyTime(4, 40, 0)
    test(t1 == t2)              # Test the equivalency operator
    test(str(t1) == "(2:20:0)")  # test the sring operator
    test(t1 + t2 == t3)
    test(t3 - t2 == t1)
    test(t3 > t1)
    t1.increment(60)
    test(t1.minutes == 21)
    t1.increment(-60)
    test(t1.minutes == 20)
    t1.increment(3600)
    test(t1.hours == 3)
    test(t1.between(t2, t3))


test_suite()