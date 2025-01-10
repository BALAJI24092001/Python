class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.main = None

    def append_(self, val):
        temp = None
        if self.main is None:
            self.main = Node(val)
            return
        else:
            temp = self.main
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(val)

    def print_(self):
        temp = None
        if self.main is None:
            print("Singly Linked List is Empty")
            return
        else:
            temp = self.main
        while temp is not None:
            print("_" * 12)
            print("|" + f"{temp.val}".center(10) + "|")
            print("־" * 12)
            print("|".center(12))
            print("V".center(12))
            temp = temp.next

    def prepend_(self, val):
        temp = self.main
        self.main = Node(val)
        self.main.next = temp

    def delete_(self, value):
        """
        Give the value in the list to be deleted from the list.
        """
        temp = self.main
        if temp is None:
            print("No values in the List!")
            return
        while temp is not None:
            if temp.next is not None:
                if temp.next.val == value:
                    temp.next = temp.next.next
                    return
                else:
                    temp = temp.next


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append_(2)
    ll.append_(2)
    ll.prepend_(1)
    ll.delete_(2)
    ll.append_(3)
    ll.append_(4)
    ll.print_()
