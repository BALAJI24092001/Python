# Take three values from user and find the biggest value.

a = int(input("Enter 1st number: "));
b = int(input("Enter 2nd number: "));
c = int(input("Enter 3rd number: "));

if b>a and b>c:
    print("b is greatest number.");
elif a>b and a>c:
    print("a id greatest number.");
elif a==b and b==c and c==a:
    print("all values are same.");
else:
    print("c is grestest number.");