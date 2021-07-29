def count_substring(string, sub_string):
    subs = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            test = 0
            for j in range(len(sub_string)):
                if i+j < len(string) and string[i+j] == sub_string[j]:
                    test = test + 1
                else:
                    break
            if test == len(sub_string):
                subs = subs + 1
    return subs


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
