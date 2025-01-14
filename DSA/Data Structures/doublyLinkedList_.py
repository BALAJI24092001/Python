class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.main = None

    def append_(self, val):
        if self.main is None:
            self.main = Node(val)
            return
        temp = self.main
        while temp is not None:
            if temp.next is None:
                temp.next = Node(val)
                temp.next.prev = temp
                return
            else:
                temp = temp.next

    def print_(self):
        temp = None
        if self.main is None:
            print("Doubly Linked List is Empty")
            return
        else:
            print("Doubly Linked List")
            temp = self.main
        while temp is not None:
            print("_" * 12)
            print("|" + f"{temp.val}".center(10) + "|")
            print("־" * 12)
            print("  ʌ".center(12))
            print("| |".center(12))
            print("V  ".center(12))
            temp = temp.next

    def delete_(self, value):
        if self.main.val == value:
            self.main = self.main.next
        temp = self.main
        if temp is not None:
            while temp is not None:
                if temp.val == value:
                    temp.prev.next = temp.next
                    return
                else:
                    temp = temp.next

    def prepend_(self, val):
        self.main.prev = Node(val)
        self.main.prev.next = self.main
        self.main = self.main.prev


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append_(1)
    dll.append_(2)
    dll.append_(2)
    dll.append_(3)
    dll.prepend_(0)
    dll.delete_(2)
    dll.print_()
