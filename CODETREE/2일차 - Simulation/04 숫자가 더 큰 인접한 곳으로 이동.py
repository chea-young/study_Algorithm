"""
NOTE
- 상 하 좌 우
- 조건: 현재 위치보다 크면 그 위치로 이동.
"""
num, row, col = tuple(map(int, input().split()))
row = row-1
col = col-1
grid = [[0 for _ in range(num)] for _ in range(num)]

for r in range(num):
    temp = list(map(int, input().split()))
    for c in range(num):
        grid[r][c] = temp[c]

def check(row, col, max_num):
    #상
    if row-1 > -1 :
        if grid[row-1][col] > max_num:
            return grid[row-1][col], row-1, col
    #하
    if row+1 < num :
        if grid[row+1][col] > max_num:
            return grid[row+1][col], row+1, col
    #좌
    if col-1 > -1:
        if grid[row][col-1] > max_num:
            return grid[row][col-1], row, col-1      
    #우
    if col+1 < num:
        if grid[row][col+1] > max_num:
            return grid[row][col+1], row, col+1
    return None, None, None
    
ans = [grid[row][col]]
check_num = 0
while True:
    check_num, row, col = check(row, col, grid[row][col])
    if check_num != None:
        ans.append(check_num)
    else:
        break

for element in ans:
    print(element, end=' ')
