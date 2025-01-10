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
    IsEmpty_()
        Return a boolean value based on the size of the stack.
    print()
        Prints the value in the stack in the stack format.
    """

    def __init__(self):
        self.lst = []

    def push_(self, a):
        self.lst.append(a)

    def pop_(self):
        if not self.IsEmpty_():
            return self.lst.pop()
        else:
            return "Stack is Empty!"

    def size_(self):
        return len(self.lst)

    def peek_(self):
        if not self.IsEmpty_():
            return self.lst[-1]
        else:
            print("Stack is Empty!")

    def Isempty_(self):
        return True if len(self.lst) == 0 else False

    def print_(self):
        if not self.IsEmpty_():
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
    a.push_(1)
    a.push_(2)
    a.push_(3)
    a.push_(5)
    print(f"Popped an item off the stack: {a.pop_()}")
    a.push_(4)
    a.push_(5)
    print(f"Size of the stack is : {a.size_()}")
    a.print_()
