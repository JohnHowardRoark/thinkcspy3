# How to Think Like a Computer Scientist: Learning with Python 3
# Wentworth et al 2012
# Chapter 03 Exercise 01


# this version does not create new lines because there is only one print called
print("We like Python's turtles! " * 1000)

# this version creates 1000 lines because the new line character is used
print("We like Python's turtles!\n" * 1000)

#this version creates 1000 lines because the print fucntion is called 1000 times
for i in range(1000):
  print("We like Python's turtles! ")