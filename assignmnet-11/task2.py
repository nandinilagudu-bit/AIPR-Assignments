class Queue:
    """Simple Queue implementation using a Python list."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            return "Error: Queue is empty."
        return self.items.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())   # 10
print(q.dequeue())   # 20
print(q.dequeue())   # Error: Queue is empty.9