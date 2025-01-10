class queue:
    def __init__(self):
        self.lst = []

    def push_(self, val):
        self.lst.append(val)

    def pop_(self, val):
        if not self.IsEmpty_():
            self.lst = self.lst[1:]
        else:
            print("Queue is Empty!")

    def size_(self):
        return len(self.lst)

    def print_(self):
        if not self.IsEmpty_():
            print("\n" + "Queue".center(12))
            for i in range(len(self.lst) - 1, -1, -1):
                string = "\n " + "_" * 10 + "\n|" + str(self.lst[i]).center(10) + "|"
                print(string, end="")
        else:
            print("Stack is Empty!")

        print("------->")

    def IsEmpty_(self):
        return True if len(self.lst) == 0 else False


if __name__ == "__main__":
    a = queue()
    a.push_(5)
    a.push_(3)
    a.push_(2)
    a.push_(1)
    a.print()
