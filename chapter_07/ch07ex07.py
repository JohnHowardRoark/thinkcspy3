""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 07 Exerciss 07 - 10
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


def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


def print_triangular_numbers(n):
    ans = 0
    for i in range(n):
        ans = ans + (i + 1)
        print((i + 1), "    ", ans)

def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            return True


def test_suite():
    """ Test suite for code in this module.
        """
    test(is_prime(11) == True)
    test(not is_prime(35) == False)
    test(is_prime(19911121) == True)    


test_suite()
sqrt(25)
print_triangular_numbers(5)