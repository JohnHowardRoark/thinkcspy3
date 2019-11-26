""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 11: Exercises 05 - 08
"""
import sys


def add_vectors(u, v):
    temp = []
    for i in range(len(u)):
        temp.append(u[i] + v[i])
    return temp


def scalar_mult(s, v):
    temp = []
    for i in range(len(v)):
        temp.append(s * v[i])
    return temp


def dot_product(u, v):
    temp = 0
    for i in range(len(u)):
        temp = temp + u[i] * v[i]
    return temp


def cross_product(u, v):
    return [(u[1] * v[2] - u[2] * v[1]), 
            (u[2] * v[0] - u[0] * v[2]), 
            (u[0] * v[1] - u[1] * v[0])]


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
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    test(cross_product([3, -3, 1], [4, 9, 2]) == [-15, -2, 39])
    test(cross_product([3, -3, 1], [-12, 12, -4]) == [0, 0, 0])

test_suite()