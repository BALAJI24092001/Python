# Print all the numbers form 1 to 100 except the multiples of 3 or 5.

for i in range(1, 101):
    if i%3 == 0 or i%5 ==0:
        continue;
    else:
        print(i,end="   ");