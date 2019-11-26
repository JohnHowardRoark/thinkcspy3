""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 07 Exercises
"""

import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = ("Test at line {0} FAILED" .format(linenum))
    print(msg)


def num_digits(n):
    """ Exercise 14: Modify num_digits so 0 returns 1 and negative numbers
        work. 
    """
    if n == 0:
        return 1
    count = 0
    while n != 0:
        count = count + 1
        n = abs(n // 10)
    return count


def num_even_digits(n):
    """ Exercise 15: Function that counts the number of even digits in n
    """
    string = str(n)
    count = 0
    for i in range(len(string)):
        if int(string[i]) % 2 == 0:
            count += 1
    return count

def sum_of_squares(xs):
    """ Exercise 16: Function that returns the sum of the squares of the numbers in a list.
    """
    sum = 0
    for i in range(len(xs)):
        sum = sum + (xs[i] ** 2)
    return sum


def test_suite():
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


test_suite()