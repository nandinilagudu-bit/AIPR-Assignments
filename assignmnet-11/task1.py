class Stack:
    """Simple Stack implementation using a Python list."""
    def __init__(self):
        self.items = []
    def push(self, item):
        """Insert an item onto the stack."""
        self.items.append(item)
    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            return "Error: Stack is empty."
        return self.items.pop()
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Error: Stack is empty."
        return self.items[-1]
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
s = Stack()
s.push(10)
s.push(20)
print(s.peek())    # 20
print(s.pop())     # 20
print(s.pop())     # 10
print(s.pop()) 