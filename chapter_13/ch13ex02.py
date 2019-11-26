""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 13: Exercise 02
"""

f = open("ex02_input_file.txt", "r")

while True:
    line = f.readline()
    if len(line) == 0:
        break
    if "snake" in line:
        print(line, end = "")

f.close()