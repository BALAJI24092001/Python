class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.head = False


class CircularLinkedList:
    def __init__(self):
        self.main = None

    def append_(self, val):
        if self.main is None:
            self.main = Node(val)
            self.main.prev = self.main
            self.main.head = True
            return
        elif self.main.next is None:
            temp = Node(val)
            self.main.next = temp
            temp.prev = self.main
            temp.next = self.main
        temp = Node(val)
        temp.prev = self.main.prev
        self.main.prev = temp
        temp.next = self.main

    # # This function is not working FIX:
    # def prepend_(self, val):
    #     temp0 = self.main
    #     temp1 = self.main.prev

    # FIX: this functionality
    def print_(self):
        """
        This is testing for implemtation using telescope.
        todo is not working in comments
        """
        temp = self.main
        if temp is None:
            print("Circular Linked List is Empty")
            return
        print("  ʌ".center(12))
        print("| |".center(12))
        print("V  ".center(12))
        while temp.val:
            print("_" * 12)
            print("|" + f"{temp.val}".center(10) + "|")
            print("־" * 12)
            print("  ʌ".center(12))
            print("| |".center(12))
            print("V  ".center(12))
            if not temp.next.head:
                break
            temp = temp.next


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append_(1)
    cll.append_(2)
    cll.append_(2)
    cll.append_(3)
    # cll.prepend_(0)
    cll.print_()
