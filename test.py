val = str(input())
lst = list()
for i in val:
    lst.append(int(i))
for i in range(len(lst) - 1):
    print(lst[i+1] - lst[i], end="")
