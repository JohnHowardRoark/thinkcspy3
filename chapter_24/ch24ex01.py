""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 24: Exercise 01: Modify print_list so output is in the format
    of [1, 2, 3]
"""

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def print_list(self):
        print("[", end="")
        self.head.print_list()
        print("]")

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()


class Node:
    
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

    def print_list(self):
        while self is not None:
            if self.next == None:
                print(self, end="")
            else:
                print(self, end=", ")
            self = self.next


def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second


link = LinkedList()
link.add_first(3)
link.add_first(2)
link.add_first(1)
link.print_list()

