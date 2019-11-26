""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 14: Exercise 04: Adapt the queens proigram to return only cases from unique famlilies.
"""

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def mirror_y(a):
    """ Exercise 4a: mirror solution in the Y axis
    """
    temp = list(a)      # copy as a list, really important
    temp.reverse()
    return temp


def mirror_x(a):
    """ Exercise 4b: mirror solution in the X axis
    """
    temp = list(a)
    for i in range(len(temp)):
        temp[i] = len(temp) - 1 - temp[i]
    return temp


def rotate_90(a):
    """ Exercise 4c: rotate 90 degrees anti-clockwise
    """
    temp = list(a)
    for i in range(8):
        temp[i] = 7 - a.index(i)
    return temp


def rotate_180(a):
    """ Exercise 4c: use rotate 90 to rotate 180
    """
    return rotate_90(rotate_90(a))


def rotate_270(a):
    """ Exercise 4c: use rotate 90 to rotate 270
    """
    return rotate_90(rotate_90(rotate_90(a)))


def rotate_360(a):
    """ Exercise 4c bonus: if rotating function works this should return the same list
    """
    return rotate_90(rotate_90(rotate_90(rotate_90(a))))


def rotate_90s(a, n):
    """ Exercise 4c bonus 2: Isn't this better?
    """
    temp = list(a)
    for i in range(n):
        temp = list(rotate_90(temp))
    return temp


def symmetries(a):
    """ Exercise 4d: generate list of symmetries of a given solution
    """
    global sols

    temp = []
    temp.append(list(a))    # don't forget to append bd as a list
    temp.append(rotate_90s(a, 1))
    temp.append(rotate_90s(a, 2))
    temp.append(rotate_90s(a, 3))
    temp.append(mirror_y(a))
    temp.append(rotate_90s(mirror_y(a), 1))
    temp.append(rotate_90s(mirror_y(a), 2))
    temp.append(rotate_90s(mirror_y(a), 3))
    temp.append(mirror_x(a))
    temp.append(mirror_x(rotate_90(a)))
    temp.append(mirror_x(rotate_180(a)))
    temp.append(mirror_x(rotate_270(a)))
    
    for i in range(len(temp)):
        if temp[i] not in sols:
            sols.append(temp[i])


def main():
    global sols
    import random
    rng = random.Random()
    bd = list(range(8))
    num_found = 0
    tries = 0
    while num_found < 12:   # making this > 12 results in infinite loop
        rng.shuffle(bd)
        tries += 1
        if bd in sols:
            continue
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            symmetries(bd)
            tries = 0
            num_found += 1


sols = []
main()

