class SelectionSort:
    def __init__(self):
        self.ops = 0

    def selectionSort_(self, arr):
        for i in range(len(arr)):
            minIndex = i
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr


if __name__ == "__main__":
    lst = [4, 3, 4, 2, 5, 2, 5, 6]
    ss = SelectionSort()
    print(ss.selectionSort_(lst))
