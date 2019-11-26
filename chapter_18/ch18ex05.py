""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 18: Exercises 05, 06, 07
"""

def recursive_min(lst):
    """ Exercise 05: Function to return the smallest value in a nested
        number list.
    """
    min = None
    first_time = True
    for i in lst:
        if type(i) == list:
            val = recursive_min(i)
        else:
            val = i

        if first_time or val < min:
            min = val
            first_time = False

    return min


def rmin(lst):
    """ Another way to do exercise 05. """
    return min(x if isinstance(x, int) else rmin(x) for x in lst)


def count(target, lst):
    """ Exercise 06: Return the number of occurrences of a target in 
        a nest list.
    """
    total = 0
    for i in lst:
        if type(i) == list:
            total += count(target, i)
        elif i == target:
            total += 1

    return total


def flatten(lst):
    """ Exercise 07: Function to flatten a nested list. """
    new = []
    for i in lst:
        if type(i) == list:
            new = new + flatten(i)
        else:
            new.append(i)
    return new


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
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
    test(rmin([2, 9, [1, 13], 8, 6]) == 1)
    test(rmin([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(rmin([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(rmin([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
    # test(count(2, []), 0) this test case is incorrect in textbook
    test(count(2, []) == 0) # corrected test case
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])


test_suite()
