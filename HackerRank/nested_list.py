# # // Not complete



# def Sort(sub_li):
#     l = len(sub_li)
#     for i in range(0, l):
#         for j in range(0, l-i-1):
#             if (sub_li[j][1] > sub_li[j + 1][1]):
#                 tempo = sub_li[j]
#                 sub_li[j]= sub_li[j + 1]
#                 sub_li[j + 1]= tempo
#     for i in range(0, l):
#         for j in range(0, l-i-1):
#             if (sub_li[j][0] > sub_li[j + 1][0]):
#                 tempo = sub_li[j]
#                 sub_li[j]= sub_li[j + 1]
#                 sub_li[j + 1]= tempo
#     return sub_li


# if __name__ == '__main__':
#     lst = list();
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         lst.append([name, score])
#     lst = Sort(lst)
#     value = lst[1][1]
#     for i in range(len(lst)):
#         if value == lst[i][1]:
#             print(lst[i][0])    


if __name__ == '__main__':
    lst = list()
    for i in range(int(input())):
        name = input() 
        score = float(input()) 
        temp = [score, name]
        lst.append(temp)
    lst.sort()
    scr = list()
    for i in lst:
        scr.append(i[0])
        
    scr.sort()
    names = list()
    for i in lst:
        if scr[1] == i[0]:
            names.append(i[1])
            
    names.sort()
    for i in names:
        print(i)
