n = int(input())
mat = list()
a = -1
b = n
for i in range(n):
    temp = input().split()
    for j in range(n):
        temp[j] = int(temp[j])
    mat.append(temp)


def cirMat(a, b):
    temp1 = a
    temp2 = b
    if a == b:
        print(mat[a][a])
        return None
    else:
        while temp1 <= temp2:
            print(mat[a][temp1], end=' ')
            temp1 = temp1+1
        temp1 = a+1
        temp2 = b

        while temp1 <= temp2:
            print(mat[temp1][b], end=' ')
            temp1 = temp1+1
        temp1 = a
        temp2 = b-1

        while temp1 <= temp2:
            print(mat[b][temp2], end=' ')
            temp2 = temp2 - 1
        temp1 = a+1
        temp2 = b-1
        while temp1 <= temp2:
            print(mat[temp2][a], end=' ')
            temp2 = temp2 - 1

        # for i in range(a, b+1):
        #     print(mat[a][a+i], end=" ")
        # for i in range(a, b):
        #     if a == 0:
        #         print(mat[a+1+i][b], end=' ')
        #     else:
        #         print(mat[a+i][b], end=' ')
        # for i in range(b-1, a-1, -1):
        #     print(mat[b][i], end=' ')
        # for i in range(b-1, a, -1):
        #     print(mat[i][a], end=' ')

        # for i in range(a, b+1):
        #     print(mat[a][a+i], end=' ')
        # for i in range(b):
        #     print(mat[a+1+i][b], end=' ')
        # for i in range(b, a-1, -1):
        #     print(mat[b][a+i], end=' ')
        # for i in range(b-1, a, -1):
        #     print(mat[i][a], end=' ')


# cirMat(a, b)
while a < b:
    a = a+1
    b = b-1
    cirMat(a, b)
