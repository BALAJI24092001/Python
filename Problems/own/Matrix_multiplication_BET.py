from numpy import *
a = int(input()) #"Enter matrix length: "
arr1 = zeros((a,a))
arr2 = zeros((a,a))


# print(arr1)
# print(arr2)


# print("Enter elements of first array: ")
for i in range(a):
    for j in range(a):
        arr1[i][j] = int(input())
# print("Enter elements of second array: ")
for i in range(a):
    for j in range(a):
        arr2[i][j] = int(input())


# print(arr1)
# print(arr2)


solArr = zeros((a,a))
for i in range(a):
    for j in range(a):
        for l in range(a):
            solArr[i][j] += arr1[j][l] * arr2[l][j];

# print("Product of the matrices is: ")
print(solArr);