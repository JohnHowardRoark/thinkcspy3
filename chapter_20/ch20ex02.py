""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 20: Exercise 02: Complete the function
"""

def add_fruit(inventory, fruit, quantity=0):
    """ Add items and/or quantities to a dictionary """
    
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    
    return inventory


def test(did_pass):
    """  Print the result of a test.  """
    import sys
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        print("Test at line {0} ok." .format(linenum))
    else:
        print("Test at line {0} FAILED" .format(linenum))


def test_suite():
    """ Test suite for code in this module.
    """
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    test("strawberries" in new_inventory)
    test(new_inventory["strawberries"] == 10)
    add_fruit(new_inventory, "strawberries", 25)
    test(new_inventory["strawberries"] == 35)


test_suite()
