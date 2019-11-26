""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 14: Section 14.7
"""

import sys

def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge_both(xs, ys):
    """ merge sorted lists and return items present in both lists """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          
            return result          

        if yi >= len(ys):          
            return result

        if xs[xi] in ys:
            result.append(xs[xi])
        xi += 1
        yi += 1


def merge_first_only(xs, ys):
    """ merge sorted lists and return items present in first list but not in second
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # We're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:]) # Add remaining items from xs
            return result          # And now we're done

        if xs[xi] not in ys:
            result.append(xs[xi])
        xi += 1
        yi += 1


def merge_second_only(xs, ys):
    """ merge sorted lists and return items present in the second list but not in the first.  I feel like this is included just to see if I am paying attention.
    """
    return merge_first_only(ys, xs)


def bagdiff(xs, ys):
    """ return items from a list that are not eliminated by a matching item in a second list.  Each second list item only eliminates one item.
    """
    result = []
    i = 0

    while True:
        if i >= len(xs):            # If xs list is finished,
            return result           # We're done.

        if xs[i] in ys:
            ys.pop(ys.index(xs[i])) # If value found in ys, pop it from ys
            i += 1                  # Go to next item in xs
        else:
            result.append(xs[i])    # Append items that did not generate pop


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        print("Test at line {0} ok." .format(linenum))
    else:
        print("Test at line {0} FAILED" .format(linenum))


def test_suite():
    """ Test suite for code in this module.
    """
    test(merge(xs, []) == xs)
    test(merge([], ys) == ys)
    test(merge([], []) == [])
    test(merge(xs, ys) == zs)
    test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
    test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) == ["a", "big", "big", "bite", "cat", "dog"])
    test(merge_both(xs, ys) == [])
    test(merge_both(xs, zs) == xs)
    test(merge_both(list_a, list_b) == [1,2,3])
    test(merge_both(list_a, list_c) == [1,2,3,4,5,6,7,8,9])
    test(merge_first_only(list_a, list_b) == [4,5,6,7,8,9,10])
    test(merge_first_only(list_a, list_c) == [10])
    test(merge_second_only(list_a, list_c) == [11,12,13,14,15])
    test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])


list_a = [1,2,3,4,5,6,7,8,9,10]
list_b = [1,2,3,11,12,13]
list_c = [1,2,3,4,5,6,7,8,9,11,12,13,14,15]
xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()

test_suite()
