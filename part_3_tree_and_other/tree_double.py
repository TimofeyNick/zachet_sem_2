class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def print_binary_tree(self, node):
        if node is None:
            return
        self.print_binary_tree(node.left)
        print(node.value)
        self.print_binary_tree(node.right)

    def tree_search(self, node, key):
        if node is None:
            return
        if node.key == key:
            return node
        if key < node.key:
            return self.tree_search(node.left, key)
        else:
            return self.tree_search(node.right, key)

