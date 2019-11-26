""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 08: Exercise 06
"""


layout = "{0:>4}{1}{2:>6}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{12:>4}{13:>4}"

print(layout.format("", " ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
print(layout.format("", ":", "------", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----",))
for i in range(1, 13):
    print(layout.format(i, ":", i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i, 9*i, 10*i, 11*i, 12*i))