# cook your dish here
def fact(n):
    if n == 1:
        return 1
    else:
        n = n*fact(n-1)
        return n


p = int(input())
for i in range(p):
    val = int(input())
    print(fact(val))
