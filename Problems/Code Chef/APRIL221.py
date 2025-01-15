val = int(input())
vals = str()
a = 0;
b = 0;
for i in range(val):
    vals = str(input()).split()
    a, b = int(vals[0]), int(vals[1])
    if(a>=b):
        print('YES')
    else:
        print("NO")
