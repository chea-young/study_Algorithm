num, index = input().split()
num_list = [int(i) for i in input().split()]
num_list = sorted(num_list)
print(num_list[int(index)-1])