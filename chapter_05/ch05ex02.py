""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 02 """

def day_from_number(n):
  alist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  x = alist[n]
  return x


start = int(input("What is the starting day number?\n"))
duration = int(input("Plus how many days?\n"))
end = (start + duration) % 7
end_day = day_from_number(end)
print("Return day of week is: ", end_day)
