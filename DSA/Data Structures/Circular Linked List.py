class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.main = None
        self.head = False

    def append_(self, val):
        if self.main is None:
            self.main = Node(val)
            self.main.head = True
            self.main.prev = self.main
            return
        temp = self.main.prev
        temp.next = Node(val)
        temp.next.prev = temp
        temp.next.next = self.main

    def prepend_(self, val):
        temp = self.main.prev
        temp.next = Node(val)
        temp.next.head = True
        self.main.head = False
        self.main = temp.next

    def print_(self):
        temp = None
        if self.main is None:
            print("Circular Linked List is Empty")
            return
        else:
            temp = self.main
        print("  ʌ".center(12))
        print("| |".center(12))
        print("V  ".center(12))
        while temp is not None:
            print("_" * 12)
            print("|" + f"{temp.val}".center(10) + "|")
            print("־" * 12)
            print("  ʌ".center(12))
            print("| |".center(12))
            print("V  ".center(12))
            temp = temp.next


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append_(1)
    cll.append_(2)
    cll.append_(2)
    cll.append_(3)
    cll.prepend_(0)
    cll.print_()
