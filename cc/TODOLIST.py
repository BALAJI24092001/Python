val = int(input())
for i in range(val):
    j = int(input())
    lst = list(map(int, str(input()).split()))
    count = 0
    for k in lst:
        if(k >= 1000):
            count+=1
    print(count)
