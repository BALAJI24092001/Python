class BubbleSort:
    """
    Bubble Sort:
    ־־־־־־־־־־־
    Bubble sort algorithm, to sort an array or list in ascending order.

    Functions:
    1. bubbleSort_(arr)
        arr: list or an array
    2. timeComplexity_()

    Variables:
    1. ops: number of operations to finish the sorting on the list using Bubble Sort algorithm
    """

    def __init__(self):
        self.ops = 0

    def bubbleSort_(self, arr: list):
        """
        Sort the array using Bubble Sort Algorithm

        Attributes:
        arr: list type

        Returns a list of sorted values
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    self.ops += 1
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def timeComplexity_(self):
        """
        Returns the number of operations it took for the given list to be sorted using Bubble Sort.
        """
        print(f"Time complexity is {self.ops}")


if __name__ == "__main__":
    lst = [4, 3, 4, 2, 1, 4, 5, 2]
    bs = BubbleSort()
    print(bs.bubbleSort_(lst))
    bs.timeComplexity_()
