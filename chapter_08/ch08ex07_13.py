""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 08: Exercise 07
"""
import sys


def reverse(word):
    """ Exercise 07: Function that reverses its string argument. """
    temp = ""
    for i in range(len(word)):
        temp += word[len(word) - i - 1]
    return temp


def mirror(word):
    """ Exercise 08: Function that mirrors its argument. """
    return word + reverse(word)


def remove_letter(a, b):
    """ Exercise 09: Remove all occurrences of a given letter from a string. """
    temp = ""
    for i in range(len(b)):
        if b[i] != a:
            temp += b[i]
    return temp


def is_palindrome(word):
    """ Exercise 10: Test if argument is a palindrome. """
    if word == reverse(word):
        return True
    return False


def count(a, b):
    """ Exercise 11: Function that counts how many times a substring occurs in a string.
    """
    temp = 0
    for i in range(len(b)):
        if b.find(a, i) == i:
            temp += 1
    return temp


def remove(s, word):
    """ Exercise 12: Remove the first occurrence of a string from another string.
    """
    if word.find(s) < 0:
        return word
    return word[0:word.find(s)] + word[word.find(s)+len(s):]


def remove_all(s, word):
    """ Exercise 13: Remove all occurrences of a string from another string. """
    temp = remove(s, word)
    while remove(s, temp) != temp:
        temp = remove(s, temp)
    return temp


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
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite()