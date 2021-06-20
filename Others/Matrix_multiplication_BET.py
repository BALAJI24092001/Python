from numpy import *
a = int(input("Enter matrix length: "))
arr1 = array([[0*a]*a])
arr2 = array([[0*a]*a])
for i in range(a):
    for j in range(a):
        print(arr1[i][j], end=" ")
    print();
for i in range(a):
    for j in range(a):
        print(arr2[i][j], end=" ")
    print();
print("Enter elements of first array: ")
for i in range(0,a):
    for j in range(0,a):
        arr1[i][j] = int(input())
print("Enter elements of second array: ")
for i in range(0,a):
    for j in range(0,a):
        arr2[i][j] = int(input())

solArr = array([[0*a]*a])
c = 0;
d = 0;
for i in range(0, a*a):
    temp = 0;
    for j in range(0,a):
        for l in range(0, a):
            temp += arr1[j][l] * arr2[l][j]
        solArr[c][d];
        if c == a:
            c = 0;
        else:
            c+=1;
        if d == a:
            d = 0;
        else:
            d+=1;

for i in range(a):
    for j in range(a):
        print(solArr[i][j], end=" ")
    print();