""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 06 All exercises
"""

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


def test(num, did_pass):
    """  Print the result of a test.  """
    if did_pass:
        msg = "Test %d ok." %num
    else:
        msg = "Test %d FAILED" %num
    print(msg)


def test_suite():
    """ Test suite for code in this module.
    """
    test(1, turn_clockwise("N") == "E")
    test(2, turn_clockwise("W") == "N")
    test(3, turn_clockwise(42) == None)
    test(4, turn_clockwise("rubbish") == None)
    test(5, day_name(3) == "Wednesday")
    test(6, day_name(6) == "Saturday")
    test(7, day_name(42) == None)
    test(8, day_num("Friday") == 5)
    test(9, day_num("Sunday") == 0)
    test(10, day_num(day_name(3)) == 3)
    test(11, day_name(day_num("Thursday")) == "Thursday")
    test(12, day_num("Halloween") == None)
    test(13, day_add("Monday", 4) ==  "Friday")
    test(14, day_add("Tuesday", 0) == "Tuesday")
    test(15, day_add("Tuesday", 14) == "Tuesday")
    test(16, day_add("Sunday", 100) == "Tuesday")
    test(17, day_add("Sunday", -1) == "Saturday")
    test(18, day_add("Sunday", -7) == "Sunday")
    test(19, day_add("Tuesday", -100) == "Sunday")
    test(20, days_in_month("February") == 28)
    test(21, days_in_month("December") == 31)
    test(22, to_secs(2, 30, 10) == 9010)
    test(23, to_secs(2, 0, 0) == 7200)
    test(24, to_secs(0, 2, 0) == 120)
    test(25, to_secs(0, 0, 42) == 42)
    test(26, to_secs(0, -10, 10) == -590)
    test(27, to_secs(2.5, 0, 10.71) == 9010)
    test(28, to_secs(2.433,0,0) == 8758)
    test(29, hours_in(9010) == 2)
    test(30, minutes_in(9010) == 30)
    test(31, seconds_in(9010) == 10)
    test(32, compare(5, 4) == 1)
    test(33, compare(7, 7) == 0)
    test(34, compare(2, 3) == -1)
    test(35, compare(42, 1) == 1)
    test(36, hypotenuse(3, 4) == 5.0)
    test(37, hypotenuse(12, 5) == 13.0)
    test(38, hypotenuse(24, 7) == 25.0)
    test(39, hypotenuse(9, 12) == 15.0)
    test(40, slope(5, 3, 4, 2) == 1.0)
    test(41, slope(1, 2, 3, 2) == 0.0)
    test(42, slope(1, 2, 3, 3) == 0.5)
    test(43, slope(2, 4, 1, 2) == 2.0)
    test(44, intercept(1, 6, 3, 12) == 3.0)
    test(45, intercept(6, 1, 1, 6) == 7.0)
    test(46, intercept(4, 6, 12, 8) == 5.0)
    test(47, is_even(0) == True)
    test(48, is_even(4) == True)
    test(49, is_even(3) == False)
    test(50, is_odd(0) == False)
    test(51, is_odd(4) == False)
    test(52, is_odd(3) == True)

test_suite()

