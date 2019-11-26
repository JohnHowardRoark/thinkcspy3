""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 13: Exercise 03: Open a text file and make a copy with
    line numbers.
"""

f = open("ex03_input_file.py", "r")
g = open("ex03_output_file.txt", "w")
line_num = 0

while True:
    line = f.readline()
    if len(line) == 0:
        break
    line_num += 1
    g.write("{0:>4} ".format(line_num) + line)

f.close()
g.close()