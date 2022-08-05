val = int(input())
a, b, c = 0, 0, 0
s = list()
for i in range(val):
    s.append(input())
for i in range(val):
    a, b, c = map(int, s[i].split())
    if a+c <= b:
        print("YES")
    else:
        print("NO")
