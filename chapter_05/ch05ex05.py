""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 05 """


def func(p,q,r):
    return ((not(p and q)) or r)

print(func(False, False, False))
print(func(False, False, True))
print(func(False, True, False))
print(func(False, True, True))
print(func(True, False, False))
print(func(True, False, True))
print(func(True, True, False))
print(func(True, True, True))
