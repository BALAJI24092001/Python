# # cook your dish here
# n = int(input())
# a = list()
# b = list()
# ca = 0
# cb = 0
# for i in range(n):
#     x, y = map(int, input().split(' '))
#     ca = ca + x
#     cb = cb + y
#     if ca > cb:
#         a.append(ca-cb)
#     else:
#         b.append(cb-ca)
# a.sort()
# b.sort()
# # print(a)
# # print(b)
# if a[-1] > b[-1]:
#     print( "1", a[-1])
# else:
#     print("2",b[-1])


n = int(input())
p1 = 0
p2 = 0
c = 0
d = 0
for i in range(n):
    a, b = map(int, input().split())
    c += a
    d += b
    if(c > d):
        if(p1 < c-d):
            p1 = c-d
    else:
        if(p2 < d-c):
            p2 = d-c
if(p1 > p2):
    print(1, p1)
else:
    print(2, p2)
