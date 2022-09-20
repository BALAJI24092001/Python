### Array data type using inbuilt functions
from array import *
arr = array("i", [1, 2, 3, 4, 5])
# arr = array(typecode, iterable)

#    Typecode 	C Type 	                Python Type 	Minimum size in bytes
#    'b'     	signed char 	        int 	            0
#    'B'     	unsigned char 	        int             	1
#    'u'     	PY-UNICODE 	            Unicode character 	2
#    'h'     	signed short 	        int 	            2
#    'H'     	unsigned short 	        int 	            2
#    'i'     	signed int 	            int 	            2
#    'I'     	unsigned int 	        int 	            2
#    'l'     	signed long 	        int 	            4
#    'L'     	unsigned long 	        int 	            4
#    'q'     	signed long long 	    int 	            8
#    'Q'     	unsigned long long 	    int 	            8
#    'f'     	float 	                float 	            4
#    'd'     	double 	                float 	            8

# accessing array elements
print(arr[0])
print(arr[1])
for i in arr:
    print(i, end=" ")
# 1 2 3 4 5
print()

# insertion option
arr.insert(1, 60)
# 1 60 2 3 4 5

# deletion operation
arr.remove(4)
# 1 60 2 3 5

#search operation
print(arr.index(3))
# 3

# update operation
arr[1] = 66

for i in arr:
    print(i, end=" ")
# 1 66 2 3 5


### Array implementation using classes
class Array:
    def __init__(self, elements):
        pass


