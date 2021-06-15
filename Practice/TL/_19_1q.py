# Take input from user and find whether its positive or negative

import math as m
a = str(int(input("Enter any number: ")))
if m.fabs(a) == a :
    print("Positive Number");
else:
    print("Negative number");