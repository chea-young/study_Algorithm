num_str = input()
num_list = num_str.split()
num_list = [int(i) for i in num_list]

count = 0
for i in range(num_list[0], num_list[1]+1):
    div_cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            div_cnt +=1
    if(div_cnt ==3):
        count +=1
        
print(count)