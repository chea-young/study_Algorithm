num = input()
rever_num = ''
for i in range(len(num)-1, -1, -1):
    rever_num += num[i]
    
print(int(rever_num))