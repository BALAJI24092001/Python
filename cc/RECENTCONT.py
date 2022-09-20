i = int(input())
for j in range(i):
    val = int(input())
    st38 = 0;
    lm108 = 0;
    vals = str(input()).split()
    for k in vals:
        if(k == "START38"):
            st38 += 1
        else:
            lm108 += 1
    print(str(st38) + " " + str(lm108))
