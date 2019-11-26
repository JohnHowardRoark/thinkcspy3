""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 04 Section 4.5 """

def final_amt(p, r, n, t):
  a = p * (1 + r / n) ** (n * t)
  return a

p = float(input("Principal\n"))
r = float(input("rate (decimal)\n"))
n = float(input("Number of times compounded\n"))
t = float(input("Number of years\n"))

print(int(final_amt(p, r, n, t)))