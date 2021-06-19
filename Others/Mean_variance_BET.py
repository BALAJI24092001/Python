from array import *
a = int(input("Enter number of observations: "));
arr = array('f',[])

for i in range(a):
    arr.append(int(input()))

print("x","\t","x - xbar",'\t',"(x-xbar)^2");

b = 0;
for i in arr:
    b+=i;
b/=a;
c = 0;
for i in arr:
    print(i, '\t', (i - b), '\t\t', (i - b)**2)
    c+=(i-b)**2;

print();
print("mean of the sample is : ", b);
print("Variance of sample is : ", c/a);
print("For normal dist. unbiased variace estimate is (for big samples): ", b*a/(a-1))