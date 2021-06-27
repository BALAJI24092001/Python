from numpy import *
a = int(input("Enter size of arrays: "))
b = 0

while b != 1 and b != 2:
    print("1. Addition")
    print("2. Subtraction")
    b = int(input("Enter your choice: "))


arr1 = zeros((a, a))
arr2 = zeros((a, a))

print("Enter elements of 1st array: ")

for i in range(a):
    for j in range(a):
        arr1[i][j] = int(input())

print("Enter elements of 2nd array: ")

for i in range(a):
    for j in range(a):
        arr2[i][j] = int(input())

solArray = zeros((a, a))
if(b == 1):
    for i in range(a):
        for j in range(a):
            solArray[i][j] = arr1[i][j] + arr2[i][j]

elif b == 2:
    for i in range(a):
        for j in range(a):
            solArray[i][j] = arr1[i][j] - arr2[i][j]

print(solArray)
