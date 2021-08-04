in_string = input()
str_list = in_string.split()
string = str_list[0]
for i in range(int(str_list[1])):
    num = int(input()) % len(string)
    string = string[num:]+string[:num]
    # 문자열을 좌우로 뒤집기를 추가
    print(string)