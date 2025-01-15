class SelectionSort:
    def __init__(self):
        self.ops = 0

    def selectionSort_(self, arr):
        """
        Sort the array using Selection Sort Algorithm

        Attributes:
        arr: list type

        Returns a list of sorted values
        """

        leng = len(arr)
        for i in range(leng):
            minIndex = i
            for j in range(i + 1, leng):
                self.ops += 1
                if arr[minIndex] > arr[j]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

    def timeComplexity_(self):
        """
        Returns the number of operations it took for the given list to be sorted using Bubble Sort.
        """
        print(f"Time complexity is {self.ops}")


if __name__ == "__main__":
    lst = [4, 3, 4, 2, 5, 2, 5, 6]
    ss = SelectionSort()
    print(lst)
    print(sorted(lst))
    print(ss.selectionSort_(lst))
    ss.timeComplexity_()
