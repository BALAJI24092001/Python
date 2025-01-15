val = int(input())
for i in range(val):
    vals = str(input()).split()
    if int(vals[0]) < int(vals[1]) :
        print("FIRST")
    elif int(vals[0]) == int(vals[1]):
        print("ANY")
    else:
        print("SECOND")
