class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.main = None

    def append_(self, val):
        temp = self.main
        if temp is None:
            self.main = Node(val)
            return
        while temp:
            if temp.right is None and temp.val <= val:
                temp.right = Node(val)
                return
            elif temp.left is None and temp.val > val:
                temp.left = Node(val)
                return
            elif temp.right.val <= val:
                temp = temp.right
            else:
                temp = temp.left

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=" ")


if __name__ == "__main__":
    tree = BinaryTree()
    tree.append_(10)
    tree.append_(5)
    tree.append_(15)
    tree.append_(20)
    tree.append_(0)
    tree.inorder_traversal(tree.main)
    print()
    tree.preorder_traversal(tree.main)
    print()
    tree.postorder_traversal(tree.main)
