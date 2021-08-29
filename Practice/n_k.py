t = int(input())
for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    temp = n - (k - 1)
    if temp > 0 and temp % 2 != 0:
        print('Yes')
        continue
    temp = n - 2*(k-1)
    if temp > 0 and temp % 2 == 0:
        print('Yes')
    else:
        print('No')
