a = int(input("Enter number of rows: "));
c = str(input("Enter a charecter: "));
for i in range(a):
    for j in range(i+1):
        print(c[0],end=" ");
    print();

#    Output:
#    Enter number of rows: 5
#    Enter a charecter: #
#    #       
#    # #     
#    # # #   
#    # # # # 
#    # # # # #