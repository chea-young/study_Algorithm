num = int(input())

empty = ' '
for i in range(1, num+1):
    change_num = 2 * i -1
    print(empty*(num-i)+'*'*change_num)
for i in range(num-1, 0, -1):
    change_num = 2 * i -1
    print(empty*(num-i)+'*'*change_num)
    