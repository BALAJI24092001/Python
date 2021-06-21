from numpy import *
a = int(input("Enter matrix length: "))
arr1 = zeros((a,a))
arr2 = zeros((a,a))


for i in range(a):
    for j in range(a):
        print(arr1[i][j], end=" ")
    print();
for i in range(a):
    for j in range(a):
        print(arr2[i][j], end=" ")
    print();


print("Enter elements of first array: ")
for i in range(a):
    for j in range(a):
        arr1[i][j] = int(input())
print("Enter elements of second array: ")
for i in range(a):
    for j in range(a):
        arr2[i][j] = int(input())


for i in range(a):
    for j in range(a):
        print(arr1[i][j], end=" ")
    print();
for i in range(a):
    for j in range(a):
        print(arr2[i][j], end=" ")
    print();


solArr = zeros((a,a))
c = 0;
d = 0;
for i in range(a*a):
    temp = 0;
    for j in range(a):
        for l in range(a):
            temp += arr1[j][l] * arr2[l][j]
        solArr[c][d]= temp;
        if d == a:
            c+=1;
            d = 0;
        else:
            d+=1;

for i in range(a):
    for j in range(a):
        print(solArr[i][j], end=" ")
    print();