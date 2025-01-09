class queue:
    def __init__(self):
        self.lst = []

    def push(self, val):
        self.lst.append(val)

    def pop(self, val):
        if not self.isEmpty():
            self.lst = self.lst[1:]
        else:
            print("Queue is Empty!")

    def size(self):
        return len(self.lst)

    def print(self):
        if not self.isEmpty():
            print("\n" + "Queue".center(12))
            for i in range(len(self.lst) - 1, -1, -1):
                string = "\n " + "_" * 10 + "\n|" + \
                    str(self.lst[i]).center(10) + "|"
                print(string, end="")
        else:
            print("Stack is Empty!")

        print("------->")

    def isEmpty(self):
        return True if len(self.lst) == 0 else False


if __name__ == "__main__":
    a = queue()
    a.push(5)
    a.push(3)
    a.push(2)
    a.push(1)
    a.print()
