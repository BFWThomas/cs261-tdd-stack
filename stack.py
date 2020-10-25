# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Brian F Thomas

class Stack:

    def __init__(self):
        self.values = []
        self.length = -1

    def is_empty(self):
        """
        Returns whether or not the stack is empty
        """
        return self.length == -1

    def pop(self):
        """
        Removes the last item on the stack
        """
        if self.is_empty():
            raise IndexError

    def peek(self):
        """
        Looks at the last item of the stack
        """
        if self.is_empty():
            raise IndexError
        return self.values[self.length]

    def push(self, val):
        """
        Appends a new node to stack with input value
        """
        self.values += [val]
        self.length += 1