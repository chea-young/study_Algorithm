def case_1(word):
    return word[1:]+word[0]

def case_2(word):
    return word[-1] + word[:-1]

def case_3(word):
    return word[::-1]

in_string = input()
str_list = in_string.split()
word = str_list[0]
for i in range(int(str_list[1])):
    num = int(input())
    if num == 1:
        word = case_1(word)
    elif num == 2:
        word = case_2(word)
    elif num == 3:
        word = case_3(word)
    print(word)
