list1 = [1,2,3,4,5]
print(list1);
# [1, 2, 3, 4, 5]

# prints list1 like a list including the braces and commas.
for i in list1:
    print(i, end=" "); # prints only the elements in the list
# 1 2 3 4 5 

list1.append(6);
print();
print(list1); #adds only one element to the list, even if we send a list as argument to the list it adds the list as the element
#to the list
# [1, 2, 3, 4, 5, 6]

list1.append([7,8]);
print(list1);
# [1, 2, 3, 4, 5, 6, [7, 8]]

print(list1.pop()); # removes the last element of the list and returns that value
# [7,8]

print(list1.pop());
# 6

list1.extend([6,8,7]);
print(list1);
# [1, 2, 3, 4, 5, 6, 8, 7]

#extend function adds all the elements from the list passed as arguments to extend function, then directly to out mail list.
list1.reverse(); # reverses the list elemets in the usual order
print(list1);
# [7, 8, 6, 5, 4, 3, 2, 1]

list1.sort(); # sort all the elements according to the values of the list.
print(list1);
# [1, 2, 3, 4, 5, 6, 7, 8]

print(list1.index(6));# returns the index value of the elements passed to the function(which is a element of the original list)
# 5

list1.append(5);
print(list1.count(5)); # returns number of elements of same value present in the original list
# 2
