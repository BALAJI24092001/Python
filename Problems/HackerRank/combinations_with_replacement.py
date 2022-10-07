# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
msg, num = input().split(" ")
num = int(num)
lst = map(sorted, list(combinations_with_replacement(msg, num)))
lst = map("".join, lst)
for i in sorted(lst):
    for j in sorted(list(i)):
        print(j, end="")
    print()
