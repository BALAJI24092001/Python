# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = input().split()
N = int(N)
M = int(M)

for i in range(1,int((N-1)/2) +1):
    val = ( M - 3*((2*i)-1) )/2
    add = (2*i)-1 
    print("-"*(int(val)), end= "")
    print(".|."*add, end= "")
    print("-"*(int(val)), end= "")
    print()
val2 = (M-7) /2
val2 = int(val2)
print("-"*val2,end="")
print("WELCOME",end="")
print("-"*val2)
lst = list()
for i in range(1,int(((N-1)/2)+1)):
    lst.append((2*i)-1)
lst = lst[::-1]
lst2 = list()
for i in lst:
    lst2.append(M-(3*i))
# lst2 = lst2[::-1]
for i in range(int( (N-1)/2 )):
    print("-"*int(lst2[i]/2), end="")
    print(".|."*lst[i],end="")
    print("-"*int(lst2[i]/2))