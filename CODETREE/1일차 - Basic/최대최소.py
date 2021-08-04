num = int(input())
number = input()
num_list = [int(i) for i in number.split()]

min_num = min(num_list)
count = 0
for i in num_list:
    if(min_num == i):
        count +=1
print(f'{min_num} {count}')