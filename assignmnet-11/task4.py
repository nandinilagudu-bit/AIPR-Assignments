class Node:
    """Node of a Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """Simple Binary Search Tree."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        """Helper function to insert recursively."""
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
    def inorder_traversal(self):
        """Inorder traversal: Left → Root → Right."""
        self._inorder_recursive(self.root)
    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

bst.inorder_traversal()