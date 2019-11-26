# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 02 Exercise 05

p = 10000
r = .08
n = 12
t = float(input("Number of years\n"))

a = p * (1 + r / n) ** (n * t)

print("The final amount is ", int(a))