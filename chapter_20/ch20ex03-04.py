""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 20: Exercise 03: Program that creates a .txt file containing
    a frequency list of all the words in Alice in Wonderland.
    Chapter 20: Exercise 04: What is the longest word and how many
    characters does it contain?
"""

import string

""" open and read the file contents """
f = open("AliceInWonderland.txt", "r")
content_orig = f.read()
f.close()

""" convert to lower case and remove punctuation """
content_orig = content_orig.lower()
content_no_punc = ""
for letter in content_orig:
        if letter not in string.punctuation:
            content_no_punc += letter

""" convert to a list of individual items """
word_list = content_no_punc.split()

""" build dictionary """
word_count = {}
for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

""" convert to list and sort """
word_count_list = list(word_count.items())
word_count_list.sort()

""" write out to new file """
g = open("alice_words.txt", "w")
layout = "{0:<20}{1}\n"
g.write(layout.format("word", "Count"))
g.write("=========================\n")
for item in word_count_list:
    g.write(layout.format(item[0], item[1]))
g.close()

""" count letters in each word """
lst = []
for item in word_count_list:
    count = 0
    for letter in item[0]:
        count += 1
    lst.append((count, item[0]))
lst.sort(reverse = True)

""" write out to new file """
h = open("word_length.txt", "w")
layout = "{0:<45}{1}\n"
h.write(layout.format("Word", "Length"))
h.write("===================================================\n")
for item in lst:
    h.write(layout.format(item[1], item[0]))
h.close()
