"""
Last Input First Output. Stack.
"""

class Stack:
    """Stack object"""
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        """Check stack is empty!"""
        return len(self.stack) == 0

    def push(self, data):
        """Element push in stack last."""
        self.stack.append(data)
        return self.stack

    def pop(self):
        """Pop this stack last element."""
        if self.isEmpty():
            return 'Stack empty!'
        else:
            return self.stack.pop()

    def peek(self):
        """Return stack last element."""
        if self.isEmpty():
            return 'Stack empty!'
        else:
            return self.stack[-1]


stack1 = Stack()
# print(stack1.isEmpty())  # return True because stack is empty.

# print(stack1.push(1)) # return list because data push in stack and return list.


stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
# print(stack1.peek()) # return 4, because 4 this stack last element.


# print(stack1.pop()) # return 4 end stack delete 4. stack value 1,2,3.

