def binary_search(element, some_list):
    left  = 0
    right = len(some_list)-1
    num = (left+ right) //2
    index = num
    while(True):
        #print(index, left, right, num)
        if some_list[index] == element:
            return num
        elif some_list[index] > element:
            right = index
            num = (left+ right) //2
            index = num
        elif some_list[index] < element:
            left = index
            num = (left+ right+1) //2
            index = num
        if(left >= right):
            return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))