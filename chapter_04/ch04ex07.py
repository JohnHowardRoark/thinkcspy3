""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 04 Exercise 07 """

def sum_to(n):
  a = 0
  for i in range(n+1):
    a = a + i
  return a

print(sum_to(10))
