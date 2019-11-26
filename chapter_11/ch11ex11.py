""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 11: Exercise 11
"""

""" The original version did not work because the swawp used function variables, not global variables.  In that version a and b did not get swapped.  x and y were made equal to a and b, then x and y were swapped. Make global changes to carry values outside the function.
"""

def swap(x, y):
    global a, b
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)
    a = x
    b = y

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)