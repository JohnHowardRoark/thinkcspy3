""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 26: Exercise 01: Write an implementation of the Queue ADT
    using a Python list.  Compare the performance to the ImprovedQueue
    for a range of queue lengths.
"""

import time


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

    def print_queue(self):
        node = self.head.next
        print(node)
        while node.next:
            node = node.next
            print(node)


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


def test_q(list):
    """ A timed test of the Queue class using a list """
    t0 = time.perf_counter()
    
    q = Queue()
    for i in list:
        q.insert(i)

    while not q.is_empty():
        q.remove()

    t1 = time.perf_counter()
    print("Time to load and empty Queue = {0:.4f} seconds".format(t1-t0))

def test_iq(list):
    """ A timed test of the ImprovedQueue class using a list. """
    t2 = time.perf_counter()

    iq = ImprovedQueue()
    for i in list:
        iq.insert(i)

    while not iq.is_empty():
        iq.remove()

    t3 = time.perf_counter()
    print("Time to load and empty ImprovedQueue = {0:.4f} seconds".format(t3-t2))

def run_test(file):
    """ Executes the Q and IQ tests with a txt file. """
    f = open(file, "r")
    data = f.read()
    f.close()
    
    alist = data.split()
    print("Test file contains {0} items.".format(len(alist)))
    test_q(alist)
    test_iq(alist)
    print()


run_test("lorem_5_para.txt")
run_test("lorem_20_para.txt")
run_test("lorem_50_para.txt")
run_test("lorem_100_para.txt")