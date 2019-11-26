""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 13: Exercise 01
"""

f = open("ex01_input_file.txt", "r")
temp = f.readlines()
f.close()

temp = temp[::-1]

g = open("ex01_output_file.txt", "w")
for i in temp:
    g.write(i)
g.close()