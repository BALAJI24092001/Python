import random
import sys

sys.path.insert(0, "C:\\Users\\dbala\\Documents\\Projects\\Python\\DSA\\Algorithms\\")
from selectionSort_ import SelectionSort

unsorted_arrays = [[random.randint(1, 100) for _ in range(40)] for _ in range(10)]
sorted_arrays = [sorted(arr) for arr in unsorted_arrays]
ss = SelectionSort()

for i, j in zip(unsorted_arrays, sorted_arrays):
    if ss.selectionSort_(i) == j:
        print("\033[1m" + "\033[92m" + "PASS" + "\033[0m")
    else:
        print("\033[1m" + "\033[91m" + "FAILED" + "\033[0m")
