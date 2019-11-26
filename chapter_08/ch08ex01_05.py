""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 08: Exercises 01 to 05
"""
# import sys
import string


def exercise_1():
    """ Exercise 01: record the result of each of the following. """
    print("Python"[1])
    print("Strings are sequences of characters."[5])
    print(len("wonderful"))
    print("Mystery"[:4])
    print("p" in "Pineapple")
    print("apple" in "Pineapple")
    print("pear" not in "Pineapple")
    print("apple" > "pineapple")
    print("pineapple" < "Peach")


def exercise_2():
    """ Exercise 02: modify so Ouack and Quack are spelled correctly. """
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        print(letter + "u" + suffix)


def count_letters(a, b):
    """ Exercise 03: generalize the function so it accepts string and letter as arguments.
    """
    fruit = a
    count = 0
    for char in fruit:
        if char == b:
            count += 1
    return count

    
def count_letters2(a, b):
    """ Exercise 04: Re-write count_letters to use find. """
    count = 0
    for i in range(len(a)):
        if a.find(b, i, (i + 1)) == i:
            count += 1
    return count


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def analyze_string(s):
    """ Exercise 05: Remove punctuation, make into list, count words containing the letter e
    """
    alist = remove_punctuation(s).split()
    count_words = len(alist)
    count_e = 0
    for i in alist:
        if count_letters2(i, "e") > 0:
            count_e += 1
    count_pct = str(round((100 * count_e / count_words), 1)) + "%"
    print("""Your text contains %d words, of which %d (%s) contain an "e".""" %(count_words, count_e, count_pct))


quote = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare sit amet urna id ornare. Donec luctus tellus turpis, id rhoncus ligula sodales sit amet. Quisque non ante at ex placerat euismod ultricies eu massa. Donec non pellentesque erat. Vestibulum posuere et augue et consectetur. Maecenas magna dui, rutrum at lacinia ut, suscipit auctor erat. Aliquam eu vulputate nisl. Donec molestie tristique velit ut porttitor. Curabitur vestibulum, nibh non imperdiet sagittis, risus ex volutpat neque, eget facilisis mi sem id lorem.
"""



exercise_1()
exercise_2()
print(count_letters("banana", "a"))
print(count_letters2("banana", "a"))
analyze_string(quote)