if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    set_val = list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    set_val.append([i, j, k])

    vals = list()
    for i in set_val:
        if i not in vals:
            vals.append(i)
    print(vals)
