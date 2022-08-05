# cook your dish here
# x, y = input().split()
# x = int(x)
# y = float(y)
# if x%5 == 0 and x+0.50<y:
#     y = y-x-0.50
#     print(round(y, 2))
# else:
#     print(round(y, 2))

cash, balance = map(float, input().split())
if(cash % 5 != 0 or cash+0.5 > balance):
    print(balance)
else:
    print("{:.2f}".format(balance-cash-0.5))
