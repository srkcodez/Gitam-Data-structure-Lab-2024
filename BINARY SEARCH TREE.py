class Node:
    """A Node class for a binary search tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    """A binary search tree (BST) implementation."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a node with the given key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """A recursive helper function to insert a new node."""
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        else:
            print("Value already in the tree!")

    def search(self, key):
        """Search for a node containing the given key."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """Recursive helper function to search for a node."""
        if node is None:
            return False
        elif key == node.val:
            return True
        elif key < node.val:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def display_inorder(self, node):
        """Helper function to display tree contents in an inorder traversal."""
        if node:
            self.display_inorder(node.left)
            print(node.val, end=' ')
            self.display_inorder(node.right)

def main():
    bst = BinarySearchTree()
    # Insert elements
    elements = [27, 14, 35, 10, 19, 31, 42]
    for el in elements:
        bst.insert(el)

    # Display in inorder to show the BST structure
    print("Inorder traversal of BST:")
    bst.display_inorder(bst.root)
    print()

    # Perform a search
    search_key = 31
    result = bst.search(search_key)
    if result:
        print(f"Element {search_key} found in the BST.")
    else:
        print(f"Element {search_key} not found in the BST.")

if __name__ == "__main__":
    main()
