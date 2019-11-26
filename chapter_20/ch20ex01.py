""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 20: Exercise 01: Program that reads a string and returns a
    table of letters and number of occurrences, in alphabetical order.
"""

test_string = "ThiS is String with Upper and lower case Letters".lower()
letter_counts = {}
for letter in test_string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

del letter_counts[" "]

letter_items = list(letter_counts.items())
letter_items.sort()

for i in letter_items:
    print("{0}  {1}".format(i[0], i[1]))

