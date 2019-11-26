""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 01 """

def day_from_number(n):
  alist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  x = alist[n]
  return x


print(day_from_number(0))
