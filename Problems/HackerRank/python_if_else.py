# !/bin/python


# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6) and n % 2 == 0:
        print("Not Weird")
    elif n in range(6, 21) and n % 2 == 0:
        print("Weird")
    else:
        print("Not Weird")
