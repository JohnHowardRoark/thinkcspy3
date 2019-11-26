""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 07 Exercises 01 - 06
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


def count_odds(k):
    """ Returns how many odd numbers are in a list """
    tot = 0
    for i in range(len(k)):
        if k[i] % 2 != 0:
            tot += 1
    return tot


def sum_evens(k):
    """ Returns the total of all even numbers in a list """
    tot = 0
    for i in range(len(k)):
        if k[i] % 2 == 0:
            tot += k[i]
    return tot


def sum_negs(k):
    """ Returns the total of all negative numbers in a list """
    tot = 0
    for i in range(len(k)):
        if k[i] < 0:
            tot += k[i]
    return tot


def count_words(k):
    """ Return the number of words in a list that have length 5 """
    ans = 0
    for i in range(len(k)):
        if len(k[i]) == 5:
            ans += 1
    return ans


def sum_up_to_even(k):
    """ Sum all elements in a list up to first even number. This version ignores strings in list. """
    ans = 0
    for i in range(len(k)):
        if k[i].__class__ == str:  # xtra: "elements" is ambiguous
            continue
        if k[i] % 2 == 0:
            break
        ans += k[i]
    return ans


def count_to_sam(k):
    """ Count how many words are in a list up to and including the word sam """
    ans = 0
    for i in range(len(k)):
        if k[i] == "sam":
            ans += 1
            break
        ans += 1
    return ans


def test_suite():
    """ Test suite for code in this module.
    """
    test(count_odds([1, 2, 3, 4, 5]) == 3)
    test(count_odds([0]) == 0)
    test(count_odds([2, 4, 6, 8]) == 0)
    test(sum_evens([2, 4, 6, 8]) == 20)
    test(sum_evens([0]) == 0)
    test(sum_evens([1, 2, 3, 4, 5, 6, 7, 8]) == 20)
    test(sum_negs([-1, 2, -3, 4, -5]) == -9)
    test(sum_negs([1, 2, 3, 4, 5]) == 0)
    test(count_words(["aaaaa", "bbbbb", "ccccc"]) == 3)
    test(count_words(["aaaaa", "bbbbb", "ccccc"]) == 3)
    test(count_words(["aaaa", "bbbbb", "cccc"]) == 1)
    test(count_words([" "]) == 0)
    test(count_words([""]) == 0)
    test(sum_up_to_even([1, 3, 5, 6, 7]) == 9)
    test(sum_up_to_even([2, 3, 5, 7]) == 0)
    test(sum_up_to_even([1, 3, 5, 7]) == 16)
    test(sum_up_to_even(["foo", 1, 3, 5, 7, "foo"]) == 16)
    test(count_to_sam(["foo", "foo", "sam", "foo"]) == 3)
    test(count_to_sam(["sam", "foo", "sam", "foo"]) == 1)
    test(count_to_sam(["foo", "foo", "foo", "foo"]) == 4)


test_suite()