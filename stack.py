# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Brian F Thomas

class Stack:

    def __init__(self):
        self.values = []

    def is_empty(self):
        """
        Returns whether or not the stack is empty
        """
        return len(self.values) == 0
