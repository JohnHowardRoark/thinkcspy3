""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 11: Exercise 09
"""

song = "The rain in Spain..."

""" print the unmodified string """
print(song)

""" split the string, making it a list of strings """
print(song.split())

""" join puts the list back together, but the spaces are now gone """
print("".join(song.split()))

""" manually add back in the spaces during the join """
print(" ".join(song.split()))
