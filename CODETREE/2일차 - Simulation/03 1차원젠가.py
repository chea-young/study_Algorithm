num = int(input())
zenga = []    
for z in range(num):
    zenga.append(int(input()))
    
def remove_block(start, end, zenga):
    if start == end:
        zenga = zenga[:start-1] + zenga[start-1:]
    zenga = zenga[:start-1] + zenga[end:]
    return zenga

for i in range(2):
        start, end = input().split()
        zenga = remove_block(int(start), int(end), zenga)
        
print(len(zenga))
for i in zenga:
    print(i)