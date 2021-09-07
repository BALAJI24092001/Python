def nBinVal(x):

    next = 0
    if(x):
        rightOne = x & -(x)
        nextHigherOneBit = x + int(rightOne)
        rightOnesPattern = x ^ int(nextHigherOneBit)
        rightOnesPattern = (int(rightOnesPattern) /
                            int(rightOne))
        rightOnesPattern = int(rightOnesPattern) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next


n = int(input())
for i in range(n):
    x = int(input())
    print(nBinVal(x))
