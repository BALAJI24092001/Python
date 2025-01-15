# # cook your dish here
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x*fact(x-1)


# n = int(input())
# for i in range(n):
#     j = int(input())
#     print(fact(j))


n = int(input())
for _ in range(n):
    a = int(input())
    fact = 1
    for i in range(1, a+1):
        fact = fact*i
    print(fact)
