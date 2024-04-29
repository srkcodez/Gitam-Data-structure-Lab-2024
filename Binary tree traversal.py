class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self, node):
        elements = []
        if node:
            elements += self.inorder_traversal(node.left)
            elements.append(node.val)
            elements += self.inorder_traversal(node.right)
        return elements

    def preorder_traversal(self, node):
        elements = []
        if node:
            elements.append(node.val)
            elements += self.preorder_traversal(node.left)
            elements += self.preorder_traversal(node.right)
        return elements

    def postorder_traversal(self, node):
        elements = []
        if node:
            elements += self.postorder_traversal(node.left)
            elements += self.postorder_traversal(node.right)
            elements.append(node.val)
        return elements

def main():
    bt = BinaryTree()
    elements = [27, 14, 35, 10, 19, 31, 42]  # example elements to insert
    for el in elements:
        bt.insert(el)

    print("Inorder Traversal:", bt.inorder_traversal(bt.root))
    print("Preorder Traversal:", bt.preorder_traversal(bt.root))
    print("Postorder Traversal:", bt.postorder_traversal(bt.root))

if __name__ == "__main__":
    main()
