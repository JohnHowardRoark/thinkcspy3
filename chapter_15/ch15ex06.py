""" How to Think Like a Computer Scientist: Learning with Python 3
    Wentworth et al 2012
    Chapter 15: Exercise 06
"""

class SMS_store:
    """ SMS_store class stores message text and message details. """
    
    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Makes new SMS tuple, inserts it after other messages in the store. When creating this message, its has_been_viewed status is set False.
        """
        temp = False
        self.inbox.append((temp, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        """ Returns number of SMS messages in my_inbox.
        """
        return len(self.inbox)

    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages.
        """
        temp = []
        for i in range(len(self.inbox)):
            if self.inbox[i][0] == False:
                temp.append(i)
        return temp

    def get_message(self, i):
        """  Return (from_number, time_arrived, text_of_sms) for message[i]. Also change its state to "has been viewed". If there is no message at position i, return None.
        """
        if i >= len(self.inbox):
            return None
        elif i < len(self.inbox):
            temp = (True, self.inbox[i][1], self.inbox[i][2], self.inbox[i][3])
            self.inbox[i] = temp
            return (self.inbox[i][1], self.inbox[i][2], self.inbox[i][3])

    def delete(self, i):
        """ Delete the message at index i. """
        del self.inbox[i]

    def clear(self):
        """ Delete all messages from inbox. """
        self.inbox = []

    def print_inbox(self):
        """ Prints the inbox. Debug scaffolding. """
        for i in range(len(self.inbox)):
            print(self.inbox[i])


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
    my_inbox.add_new_arrival(100,"0900","This is message 1.")
    my_inbox.add_new_arrival(200,"0930","This is message 2.")
    my_inbox.add_new_arrival(300,"1000","This is message 3.")
    my_inbox.add_new_arrival(400,"1030","This is message 4.")
    my_inbox.add_new_arrival(500,"1100","This is message 5.")
    test(my_inbox.message_count() == 5)
    test(my_inbox.get_message(0) == (100,"0900","This is message 1."))
    test(my_inbox.get_unread_indexes() == [1,2,3,4])
    my_inbox.delete(4)
    test(my_inbox.message_count() == 4)
    my_inbox.clear()
    test(my_inbox.message_count() == 0)


my_inbox = SMS_store()

test_suite()
