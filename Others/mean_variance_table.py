a = int(input("Enter number of observations: "))
b = []
for i in range(a):
    c = int(input("element: "))
    b.append(c)

avg = sum(b) / len(b)
SumVariance = 0
print("x - avg", "          ", "(x-avg)**2")
for i in b:
    d = i - avg
    print(d, "          ", d**2)
    SumVariance = SumVariance + d**2
print("Mean = ", avg)
print("Variance = ", SumVariance/len(b))
