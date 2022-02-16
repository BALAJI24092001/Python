a = int(input("Enter number of rows: "));

for i in range(a):
    for j in range(a-i):
        print(" ", end=" ");
    for k in range(i+1):
        print(k+1, end=" ");
    for l in range(i,0,-1):
        print(l,end=" ");
    print();

# Output:
# Enter number of rows: 5
#           1 
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1