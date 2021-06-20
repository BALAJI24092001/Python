from numpy import *
a = int(input("Enter matrix length: "))
arr1 = array([[]*a])
arr2 = array([[]*a])
print("Enter elements of first array: ")
for i in range(a):
    for j in range(a):
        arr1[i].append(0);
for i in range(a):
    for j in range(a):
        arr1[i][j] = int(input())

for i in range(a):
    for j in range(a):
        arr2[i].append(0);

for i in range(a):
    for j in range(a):
        arr2[i][j] = int(input())

solArr = array([[]*a])
c = 0;
d = 0;
for i in range(a*a):
    temp = 0;
    for j in range(a):
        for l in range(a):
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