#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    s = list(s)
    s.sort()
    se = set(s)
    se = list(se)
    print(se)
    dic = dict()
    dic[se[0]] = 0
    dic[se[1]] = 0
    dic[se[2]] = 0
    for i in s:
        if se[0] == i:
            dic[se[0]] = dic[se[0]] + 1
        elif se[1] == i:
            dic[se[1]] = dic[se[1]] + 1
        elif se[2] == i:
            dic[se[2]] = dic[se[2]] + 1
    print(dic)
