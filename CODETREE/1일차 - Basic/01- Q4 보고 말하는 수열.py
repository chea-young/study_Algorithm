#FIX 연속한 수로 바꾸기
def make_word(num_dic):
    ans = ''
    num_list = sorted(list(num_dic.keys()))
    for i in num_list:
        ans += str(i)
        ans += str(num_dic[i])
    return ans

str_num = '1'
ans = ''
count_num = int(input())
num_dic = {}
for i in range(count_num-1):
    if count_num == 1:
        break
    num_dic = {}
    for num in str_num:
        if num in num_dic.keys():
            count = num_dic[num]
            num_dic[num] = count +1
        else:
           num_dic[num] = 1 
    str_num = make_word(num_dic)
print(str_num)

