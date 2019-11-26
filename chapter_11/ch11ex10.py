""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 11: Exercise 10
"""

import sys


def replace(s, old, new):
    return new.join(s.split(old))


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

    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()