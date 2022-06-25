# Implementing a stack which is an abstarct data type
# Created a class called stack
# The underlying data structure in a stack is a list
# the default constructor (__init__) will create a new list
# Created multiple class methods which will allow us to perform some 
# operations on the data in the list
# A stack is FIFO. We can only add and remove the data from the top of the
# stack
# The runtime (time complexity) for the push method is O(1) or constant 
# time 
# The runtime for the pop method is O(1)
# In the peek method, the best way to get the last element in the stack is
# using 'self.items[-1]' since -1 will give us the last position in the
# stack
# The runtime for peek method is O(1)
# In the size method we just return the size of the list since list is the
# underlying data structure
# The runtime for the size method is O(1)
# In the 'is_empty' method we run an equality check for the list. If the
# list is empty the output will be 'True' and if the list has elements in
# it the output will be 'False'
# the runtime for the 'is_empty' method is O(1)

class stack:

    def __init__(self):

        self.items = []

    def push(self, item):

        self.items.append(item)

    def pop(self):
        
        if self.items:
            return self.items.pop()
        
        return None

    def peek(self):

        if self.items:
            return self.items[-1]

        return None

    def size(self):
        
        return len(self.items)

    def is_empty(self):

        return self.items == []
