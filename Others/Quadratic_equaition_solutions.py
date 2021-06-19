from math import *
print("Enter cofficient of x^2 , x and the constant: ")
a = int(input())
b = int(input())
c = int(input())

if (b**2 - (4*a*c))>=0:
    d = b**2 - 4*a*c
    
    print("Roots of the given equation are: ")
    print("(",0-b,"+ root(",d,") )","/",2*a)
    print("(",0-b,"- root(",d,") )","/",2*a)
