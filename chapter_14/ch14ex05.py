""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 14: Exercise 05
"""

import sys


def lotto_draw():
    """ Exercise 5a: Return a lotto draw consisting of 6 random balls from a group numbered 1 to 49.
    """
    import random
    rng = random.Random()
    temp = list(range(1,50))
    rng.shuffle(temp)
    return temp[:6]


def lotto_match(draw, ticket):
    """ Exercise 5b: Compare a ticket and a draw and return the number of correct picks on that ticket.
    """
    temp = 0
    for i in range(len(ticket)):
        if ticket[i] in draw:
            temp += 1
    return temp


def lotto_matches(draw, tickets):
    """ Exercise 5c: Takes a list of tickets and a draw and returns a list of how many picks were correct on each ticket.
    """
    temp = []
    for i in range(len(tickets)):
        temp.append(lotto_match(draw, tickets[i]))
    return temp


def primes_in(a):
    """ Exercise 5d: Return the number of primes in a list of numbers.
    """
    temp = []
    for i in range(len(a)):
        is_prime = True
        if a[i] == 1:
            is_prime = False
        for r in range(2, a[i]-1):
            if a[i] % r == 0:
                is_prime = False
        if is_prime:
            temp.append(a[i])
    return len(temp)


def prime_misses(a):
    """ Exercise 5e: Look for missing prime numbers in the list my_tickets.
    """
    new_list = []
    for i in range(len(my_tickets)):
        for j in range(len(my_tickets[i])):
            new_list.append(my_tickets[i][j])
    temp = []
    for i in range(2, 50):
        is_prime = True
        for r in range(2, i-1):
            if i % r == 0:
                is_prime = False
        if is_prime:
            if i not in new_list:
                temp.append(i)
    return temp


def repeat_draws(n):
    """ Exercise 5f: Function that repeatedly makes new draws and compares them to the 4 tickets in my_tickets.
    """
    num_draws = 0
    while True:
        draw = lotto_draw()
        num_draws += 1
        matches = lotto_matches(draw, my_tickets)
        for i in range(len(matches)):
            if matches[i] >= n:
                return num_draws

def draw_20(n):
    """ Exercise 5f: Function to perform 20 draws and average.
    """
    temp = []
    for i in range(20):
        print(".", end = "", flush = True)
        temp.append(repeat_draws(n))
    print("\naverage of {0} draws.".format(sum(temp) // 20 + 1))


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        print("Test at line {0} ok." .format(linenum))
    else:
        print("Test at line {0} FAILED" .format(linenum))


def test_suite():
    """ Test suite for code in this module.
    """
    test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
    test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
    test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
    test(prime_misses(my_tickets) == [3, 29, 47])



my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]


# test_suite()
draw_20(4)
