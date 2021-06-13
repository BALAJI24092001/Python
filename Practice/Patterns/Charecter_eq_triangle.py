a = int(input("Enter number of rows: "));
c = str(input("Enter a charecter: "));
for i in range(a):
    for j in range(a-i):
        print(" ",end=" ");
    for k in range(2*i+1):
        print(c[0], end=" ");
    print();

#    Output:
#    Enter number of rows: 5
#    Enter a charecter: # 
#              # 
#            # # #
#          # # # # #
#        # # # # # # #
#      # # # # # # # # #