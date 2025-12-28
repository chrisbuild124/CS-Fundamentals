# This creates an iterator that iterates the next smaller value in the BST. 
# NOTE: Taken from CodePath's course 

class BSTIterator(object):
    def __init__(self, root):
        self.stack = list()
        self.push_all(root)

    def has_next(self):
        return self.stack

    def next(self):
        tmpNode = self.stack.pop()
        self.push_all(tmpNode.right)
        return tmpNode.val

    def push_all(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
