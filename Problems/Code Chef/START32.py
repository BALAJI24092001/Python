val = int(input())
for i in range(val):
    vals = str(input()).split()
    a = int(vals[0])
    b = int(vals[1])
    if a >= b:
        print(a-b)
    else:
        print(b-a)
