# cook your dish here
n = int(input())
lst = list()
for i in range(n):
    temp = int(input())
    lst.append(temp)
lst.sort()
for i in lst:
    print(i)
