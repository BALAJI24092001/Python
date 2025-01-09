class stack:
    """
    stack:
    ־־־־־־
    This is a class defined to operate on stack data type.

    Functions:
    push(val)
        Inserts a value on top of the stack.
    pop()
        Removed a value on top of the stack.
    size()
        Returns number of values available in the stack.
    peek()
        Returns the top most number in the stack.
    is_empty()
        Return a boolean value based on the size of the stack.
    print()
        Prints the value in the stack in the stack format.
    """

    def __init__(self):
        self.lst = []

    def push(self, a):
        self.lst.append(a)

    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return "Stack is Empty!"

    def size(self):
        return len(self.lst)

    def peek(self):
        if not self.is_empty():
            return self.lst[-1]
        else:
            print("Stack is Empty!")

    def is_empty(self):
        return True if len(self.lst) == 0 else False

    def print(self):
        if not self.is_empty():
            print("Stack".center(12))
            for i in range(len(self.lst) - 1, -1, -1):
                if i == len(self.lst) - 1:
                    string = (
                        "\n "
                        + "_" * 10
                        + " \n|"
                        + str(self.lst[i]).center(10)
                        + "|"
                        + "------->"
                        + "\n "
                        + "־" * 10
                    )
                else:
                    string = (
                        "\n"
                        + "|"
                        + str(self.lst[i]).center(10)
                        + "|"
                        + "\n "
                        + "־" * 10
                    )
                print(string, end="")
        else:
            print("Stack is Empty!")


if __name__ == "__main__":
    import numpy as np

    a = np.array([1, 2, 3])
    print(a)

    a = stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(5)
    print(f"Popped an item off the stack: {a.pop()}")
    a.push(4)
    a.push(5)
    print(f"Size of the stack is : {a.size()}")
    a.print()
