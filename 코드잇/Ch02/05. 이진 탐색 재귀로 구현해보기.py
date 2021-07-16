def binary_search(element, some_list, start_index=0, end_index=None, num =None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    if num == None:
        num = (start_index + end_index) //2
    #print(start_index, end_index, num)
    #print(some_list[num], element)
    if some_list[num] == element:
        #print('in1')
        return num
        
    if (start_index >= end_index):
        return None
    elif some_list[num] > element:
        #print('in2')
        return binary_search(element, some_list, start_index, num, (start_index+num)//2)
    elif some_list[num] < element:
        #print('in3')
        return binary_search(element, some_list, num, end_index, (num + end_index + 1)//2 )
    
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))