class Node:
    """Node of a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display all elements in the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)

ll.display()