class Node:
    def __init__(self, datavalue) -> None:
        self.datavalue = datavalue
        self.nextvalue = None


class SLinkedList:
    def __init__(self) -> None:
        self.headval = None

    def AtEnd(self, datavalue):
        NewNode = Node(datavalue)
        if self.headval is None:
            self.headvalue = NewNode
            return
        laste = self.headval
        while laste.nextvalue:
            laste = laste.nextvalue
        laste.nextvalue = NewNode

    def AtBeg(self, newdata):
        newnode = Node(newdata)
        newnode.nextvalue = self.headval
        self.headval = newnode

    def InBetween(self, MiddleNode, newdata):
        if MiddleNode is None:
            print("Invalid middle node")
            return
        NewNode = Node(datavalue)
        NewNode.nextvalue = MiddleNode.nextvalue
        MiddleNode.nextvalue = NewNode

    def listprint(self):
        laste = self.headvalue
        while laste is not None:
            print(laste.datavalue)
            laste = laste.nextvalue
