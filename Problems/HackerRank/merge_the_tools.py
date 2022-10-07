def merge_the_tools(string, k):
    lst = list()
    for i, j in zip( range(0, len(string), k), range(k, len(string)+1, k) ):
        lst.append(string[i:j])
    for i in lst:
        temp = list(i)
        final_temp = list()
        for i in temp:
            if i not in final_temp:
                final_temp.append(i)
        temp = "".join(final_temp)
        print(temp)        
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


#INPUT
#    AABCAAADA
#    3
#OUTPUT
#    AB
#    CA
#    AD
