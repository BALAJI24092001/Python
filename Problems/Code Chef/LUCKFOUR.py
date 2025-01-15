# cook your dish here
n = int(input())

for i in range(n):
    val = input()
    ans = 0
    for j in val:
        if j == '4':
            ans = ans + 1
    print(ans)
