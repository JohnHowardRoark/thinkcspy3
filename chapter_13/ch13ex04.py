""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 13: Exercise 04
"""

f = open("ex03_output_file.txt", "r")
g = open("ex04_output_file.txt", "w")

while True:
    line = f.readline()
    if len(line) == 0:
        break
    g.write(line[5:])

f.close()
g.close()