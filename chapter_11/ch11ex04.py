""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 11: Exercise 04
"""

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
""" first test returns false, variables are pointing to different sets """
print("Test 1: {0}".format(this is that))
""" the next statement changes variable 'that' so it points to the same set as variable 'this'"""
that = this
""" second test returns true, variables now point to the same set """
print("Test 2: {0}".format(this is that))


""" if variable is just a string, returns true """
a = "a"
b = "a"
print(a is b)

""" if variable is a set, returns false """
c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)