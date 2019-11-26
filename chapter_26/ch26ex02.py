""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 26: Exercise 02: Write an implementation of the Priority
    Queue ADT using a linked list.  Compare the performance to the
    Python list implementation.
"""

import time

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


def test_pq(split_list):
    
    t0 = time.perf_counter()
    
    pq = PriorityQueue()
    for i in split_list:
        pq.insert(i)

    pq.remove()

    t1 = time.perf_counter()
    print("Time to load PriorityQueue and return largest item = {0:.6f} seconds".format(t1-t0))

def test_list(split_list):
    
    t0 = time.perf_counter()
    
    split_list.sort()
    temp = split_list[0]
    
    t1 = time.perf_counter()
    
    print("Time to load and empty Python list and return largest item = {0:.6f} seconds".format(t1-t0))

def run_test(file):
    """ Executes the PQ with a txt file. """
    f = open(file, "r")
    data = f.read()
    f.close()
    split_list = data.split()
    print("Test file contains {0} items.".format(len(split_list)))
    test_pq(split_list)
    test_list(split_list)
    print()


run_test("lorem_5_para.txt")
run_test("lorem_20_para.txt")
run_test("lorem_50_para.txt")
run_test("lorem_100_para.txt")
run_test("lorem_1000_para.txt")
