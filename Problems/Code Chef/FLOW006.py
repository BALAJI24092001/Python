# cook your dish here
n = int(input())
for i in range(n):
    val = input()
    ans = 0
    for i in range(len(val)):
        ans = ans + int(val[i])
    print(ans)
