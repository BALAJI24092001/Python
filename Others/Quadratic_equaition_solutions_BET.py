from math import *
print("Enter cofficient of x^2, x and the constant: ")
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if d == 0:
    print("Determinant value is zero, roots are equal: ",(0-b+d)/2*a);
    # print((0-b-d)/2*a);
else:
    print("Roots of the given equation are: ")
    print("[",0-b,"+ root(",d,")]","/",2*a)
    print("[",0-b,"- root(",d,")]","/",2*a)