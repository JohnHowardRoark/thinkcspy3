""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 09: Exercise 01
"""


""" Pass a tuple as an argument to a function """


def list_celebs(i):
    print(i[0][0], "was born in", i[0][1])
    print(i[1][0], "was born in", i[1][1])


celebs = (("Paris Hilton", 1981), ("Julia Roberts", 1967))

list_celebs(celebs)
