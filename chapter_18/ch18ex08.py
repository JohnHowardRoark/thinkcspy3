""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exercise 08: Rewrite the fibonacci alogorithm without
    using recursion.
    
    Note: the fibonacci sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
    This means 55 is the 11th term.  The textbook regression function
    returns 55 for an input of 10. The non-regressive function has been 
    adjusted to match this output.
"""

import time


def fib(n):
    """ Fibonacci series using regression """
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


def my_fib(n):
    """ Fibonacci series without regression """
    a = 0
    b = 1
    for i in range(n):
        next = a + b
        a = int(b)
        b = int(next)
    return a


""" Call textbook function. 1.81 secs for n = 35 """
n = 35
t0 = time.perf_counter()
result = fib(n)
t1 = time.perf_counter()
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

""" Call new function. 0.00 secs for n = 35 """
n = 35
t0 = time.perf_counter()
result = my_fib(n)
t1 = time.perf_counter()
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

""" Call new function with n = 200. Result in 0.00 secs """
n = 200
t0 = time.perf_counter()
result = my_fib(n)
t1 = time.perf_counter()
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

""" Call new function with n = 100000. Result in 0.11 secs """
n = 100000
t0 = time.perf_counter()
result = my_fib(n)
t1 = time.perf_counter()
print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

