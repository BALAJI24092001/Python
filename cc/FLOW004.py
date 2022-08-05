val = int(input())
s = list()
for i in range(val):
    s.append(input())
for i in range(val):
    print(int(s[i][0]) + int(s[i][-1]))

