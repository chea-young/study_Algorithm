str_num = '1'
ans = ''
count_num = int(input())
for i in range(count_num-1):
    temp_str = ''
    if count_num == 1:
        break
    check = str_num[0]
    count = 0
    for i in str_num:
        if check == i:
            count +=1
        else:
            temp_str += check
            temp_str += str(count)
            check = i
            count = 1
    temp_str += check
    temp_str += str(count)
    str_num = temp_str
print(str_num)