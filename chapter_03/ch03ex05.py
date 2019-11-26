# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 03 Exercise 05

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

total = 0       # since we are adding, start at 0
product = 1     # for multiplication, we must start at 1

for i in xs:
  print(i, " ", i**2)
  total = total + i
  product = product * i

print()
print("Sum of original set is: ", total)
print("Product of original set is: ", product)