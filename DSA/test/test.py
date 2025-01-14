import sys

sys.path.insert(
    0, "C:\\Users\\dbala\\Documents\\Projects\\Python\\DSA\\Data Structures\\"
)
sys.path.insert(1, "C:\\Users\\dbala\\Documents\\Projects\\Python\\DSA\\Algorithms\\")

import binarySearchTree_ as bst
import doublyLinkedList_ as dll
import queue_
import singlyLinkedList_ as sll
import stack_

# NOTE: Stack Implementation
st = stack_.stack()
st.push_(5)
st.push_(6)
st.push_(7)
st.push_(9)
st.pop_()
print(st.size_())
st.print_()

# Note: Stack implementation
qu = queue_.queue()
qu.push_(5)
qu.push_(4)
qu.push_(3)
qu.push_(3)
qu.pop_(3)
qu.push_(2)
qu.push_(1)
qu.print_()

# NOTE: Singly Linked List Implementation
ll = sll.SinglyLinkedList()
ll.append_(2)
ll.append_(2)
ll.prepend_(1)
ll.delete_(2)
ll.append_(3)
ll.append_(4)
ll.print_()

# NOTE: Double Linked List Implementation
dll = dll.DoublyLinkedList()
dll.append_(1)
dll.append_(2)
dll.append_(2)
dll.append_(3)
dll.prepend_(0)
dll.delete_(2)
dll.print_()


# NOTE: Binary Search Tree Implementation (BST)
print("Binary Search Tree")
tree = bst.BinarySearchTree()
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
