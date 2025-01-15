class InsertionSort:
    def __init__(self):
        self.ops = 0

    def insertionSort_(self, arr: list):
        n = len(arr)
        for i in range(1, n):
            index = i
            val = arr[i]
            for j in range(i - 1, -1, -1):
                if arr[j] > val:
                    self.ops += 1
                    arr[j + 1] = arr[j]
                    index = j
            arr[index] = val
        return arr

    def timeComplexity_(self):
        """
        Returns the number of operations it took for the given list to be sorted using Insertion Sort.
        """
        print(f"Time complexity is {self.ops}")


if __name__ == "__main__":
    lst = [5, 2, 9, 1, 5]
    Inso = InsertionSort()
    print(Inso.insertionSort_(lst))
    Inso.timeComplexity_()
