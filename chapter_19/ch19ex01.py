""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 19: Exercise 01: Function that prompts the user for a positive
    integer and checks the input against requirements.
"""


def readposint():
    """ Prompts the user for a positive integer and verifies the input."""

    try:
        i = input("Enter a positive integer: ")
        if int(i) > 0:
            print("{0} is a positive integer".format(i))
        else:
            print("{0} is not positive".format(i))
    
    except:
        print("{0} is not an integer".format(i))
    
    finally:
        exit()


readposint()

