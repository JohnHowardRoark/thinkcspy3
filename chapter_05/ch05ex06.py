""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 05 Exercise 06 """

def grade(n):
  if n >= 75:
    return "First"
  elif n >=70 and n < 75:
    return "Upper Second"
  elif n >=60 and n < 70:
    return "Second"
  elif n >=50 and n < 60:
    return "Third"
  elif n >=45 and n < 50:
    return "F1 Supp"
  elif n >=40 and n < 45:
    return "F2"
  elif n < 40:
    return "F3"


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]


for i in range(len(xs)):
  print(grade(xs[i]))