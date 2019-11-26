""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 06 All exercises
"""
import sys

def turn_clockwise(i):
    """ Exercise 1: Function that takes cardinal direction and returns  correct direction after 1 clockwise turn. """
    alist = ["N", "E", "S", "W"]
    if i in alist:
        ans = (alist.index(i) + 1) % 4
        return alist[ans]
    return None


def day_name(i):
    """ Exercise 2: Convert interger into a day name """
    alist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if i >= 0 and i <= 6:
        return alist[i]
    return None

def day_num(i):
    """ Exercise 3: Convert day name into integer """
    alist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if i in alist:
        return alist.index(i)
    return None


def day_add(day, delta):
    """ Exercises 4 & 5: Funciton that takes a day name and integer number of days and returns the correct day name
    """
    return day_name((day_num(day) + delta) % 7)


def days_in_month(i):
    """ Exercise 6: Function that takes the name of the month and returns the number of days in that month
    """
    months_28 = ["February"]
    months_30 = ["April", "June", "September", "November"]
    months_31 = ["January", "March", "May", "July", "August", "October",
                 "December"]
    if i in months_28:
        return 28
    elif i in months_30:
        return 30
    elif i in months_31:
        return 31
    else:
        return None
    

def to_secs(h, m, s):
    """Exercises 7 & 8: Convert hours, minutes and seconds to total number of seconds. Make it always return an integer.
    """
    return int(h * 3600 + m * 60 + s)


def hours_in(s):
    """ Exercise 9: Takes total number of seconds and returns whole integer number of hours, minutes and seconds.
    """
    return int(s / 3600)


def minutes_in(s):
    """ Part of exercise 9 """
    return int((s - (hours_in(s) * 3600)) / 60)


def seconds_in(s):
    """ Part of exercise 9 """
    return s - (hours_in(s) * 3600) - (minutes_in(s) * 60)


def compare(a, b):
    """ Exercise 11 """
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0


def hypotenuse(a, b):
    """ Exercise 12: Return the length of the hypotenuse of a right triangle given the lengths of the other two sides. """
    return (a ** 2 + b ** 2) ** 0.5


def slope(x1, y1, x2, y2):
    """ Exercise 13: Function that returns the slope of a line through two points """
    return (y2 - y1) / (x2 - x1)

def intercept(x1, y1, x2, y2):
    """ Exercise 13: Function that returns the y-intercept of a line through two points, using slope function """
    m = slope(x1, y1, x2, y2)
    b = y1 - (m * x1)
    return b


def is_even(n):
    """ Exercise 14: Function that returns True for an even number and False for odd. """
    if n % 2 == 0:
        return True
    return False


def is_odd(n):
    """ Exercise 15: Use a function call to is_even to test for odd """
    if is_even(n) == True:
        return False
    return True


def is_factor(f, n):
    """ Exercise 16: Write a function that passes the tests listed """
    if n % f == 0:
        return True
    return False


def is_multiple(a, b):
    """ Exercise 17: Use is_factor to pass the tests listed """
    if is_factor (b, a) == 0:
        return False
    return True


def f2c(t):
    """ Exercise 18: Function that converts Fahrenheit to Celsius """
    return round((t - 32) * 5 / 9)


def c2f(t):
    """ Exercise 19: Function that converts Celsius to Fahrenheit """
    return round(t * 9 / 5 + 32)


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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(0) == True)
    test(is_even(4) == True)
    test(is_even(3) == False)
    test(is_odd(0) == False)
    test(is_odd(4) == False)
    test(is_odd(3) == True)
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


test_suite()

