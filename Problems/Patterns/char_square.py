n = int(input("Enter size of sqlare: "))
for i in range(n):
    if i == 0 or i == n-1:
        for i in range(n):
            print("* ", end="")
        print()
    else:
        print("* ", end="")
        for i in range(n - 2):
            print("  ", end="")
        print("* ")

#    Output:

#    Enter size of sqlare: 5
#    * * * * * 
#    *       * 
#    *       * 
#    *       * 
#    * * * * * 
