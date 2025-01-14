class BinarySearch:
    """
    Binary Search Class:
    ־־־־־־־־־־־־־־־־־־־
    Binary Search opeartion on given array.

    Functions:
    1. binarySearch_(arr: list(), tar)
        arr: list or an array
        tar: value to search in the list
    2. timeComplexity_()

    Variables:
    1. ops: number of operations to finish the searching process for the given list using binary search algorithm

    """

    def __init__(self):
        self.ops = 0

    def binarySearch_(self, arr: list, tar):
        """
        Attributes:
        arr: List or array type
        tar: Target variable to search from the list

        Returns an index position for the tar variable value
        """
        print(f"Binary Search \nList: {arr}\nValue: {tar}")
        self.ops += 1
        right = len(arr)
        left = 0
        for i in range(len(arr)):
            temp = (left + right) // 2
            if tar == arr[temp]:
                self.ops += 1
                return f"Index : {temp}"
            elif tar > arr[temp]:
                left = (left + right) // 2
            else:
                right = (left + right) // 2
        return "No such value exist in the given list."

    def timeComplexity_(self):
        print(f"Time complexity is {self.ops}")


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    bs = BinarySearch()
    print(bs.binarySearch_(lst, 7))
    bs.timeComplexity_()
