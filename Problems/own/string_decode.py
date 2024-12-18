#String Problem
#
#Description In a certain encrypted message which has information about the location(area, city), the characters are jumbled such that the first character of the first word is followed by the first character of the second word, then it is followed by the second character of the first word and so on.
#
#In other words, let’s say the location is bandra,mumbai
#
#The encrypted message says ‘bmaunmdbraai’.
#
#Sample Input:
#
#bmaunmdbraai
#
#Sample Output:
#
#bandra,mumbai
#
#Let’s say the size or length of the two words wouldn’t match, then the smaller word is appended with # and then encrypted in the above format.
#
#With this in mind, write a code to identify the right location and print it as place, city.


msg = input()
w1 = list()
w2 = list()
i = 0;
while i < len(msg):
    if(msg[i] != "#"):
        w1.append(msg[i])
    if(msg[i+1] != "#"):
        w2.append(msg[i+1])
    i += 2
print(f"{''.join(w1)}, {''.join(w2)}")
