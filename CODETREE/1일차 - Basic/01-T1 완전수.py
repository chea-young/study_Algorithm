def find_divisor(num):
    ans = []
    for i in range(1, num):
        if num%i == 0:
            ans.append(i)
    return ans

start, end = input().split()
count = 0
for i in range(int(start), int(end)+1):
    num_list = find_divisor(i)
    if i == sum(num_list):
        count +=1
print(count)