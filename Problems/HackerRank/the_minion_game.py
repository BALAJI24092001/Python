
#import itertools
#def minion_game(string):
#    strn = list(string)
#    vow = list()
#    cons = list()
#    for i in strn:
#        if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
#            vow.append(i)
#        else:
#            cons.append(i)
#    allval = list()
#
##    for i in range(len(strn)+1):
##        for j in itertools.permutations(strn, i):
##            allval.append("".join([str(val) for val in j ]))
##    allval.remove("")
##    stu_val = list()
##    for i in allval:
##        if i[0] in cons:
##            stu_val.append(i)
#    
##    kev_val = list()
##    for i in allval:
##        if i[0] in vow:
##            kev_val.append(i)
#    
##    kev_val = set(kev_val)
##    stu_val = set(stu_val)
#    
#    words_stu = list()
#    for i in range(len(strn)):
#        for j in range(i, len(strn)+1):
#            if string[i:j] != "":
#                words_stu.append(string[i:j])
#   
#    kev_val = list()
#    for i in words_stu:
#        if i[0] in vow:
#            kev_val.append(i)
#
#    stu_val = list()
#    for i in words_stu:
#        if i[0] in cons:
#            stu_val.append(i)
#
#
#    stu_sco = 0
#    for i in stu_val:
#        for j in words_stu:
#            if i == j:
#                stu_sco += 1
#    
#    kev_sco = 0
#    for i in kev_val:
#        for j in words_stu:
#            if i == j:
#                kev_sco += 1
#
#    if stu_sco > kev_sco:
#        print(f"Stuart {stu_sco}")
#    elif kev_sco > stu_sco:
#        print(f"Kevin {kev_sco}")
#    else:
#        print("Draw")
def minion_game(string):
    # your code goes here
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if string[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
