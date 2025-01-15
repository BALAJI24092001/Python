s = list(map(int, str(input()).split()))
count = 0
for i in s:
    if i>=10:
        count += 1
    
print(count)
