"""
NOTE 
- 좌측모서리를 완전탐색을 하면서 탐색해가는 것.
- 한 위치를 잡았다고 하면 그 격자 안에서 동전의 위치를 세는 방법
- 또 다른 방법으로는 padding을 추가하는 방법이 존재.
"""
n = int(input())
grid = [[int(i) for i in input().split()] for j in range(n)]

def cal_count(start_r, end_r, start_c, end_c):
    count = 0
    for i in range(start_c, end_c+1):
        for j in range(start_r, end_r+1):
            if grid[i][j] == 1:
                count += 1
    return count

ans = 0
for col in range(n):
    for row in range(n):
        if col+2 >= n or row+2 >= n:
            continue
        check = cal_count(row, row+2, col, col+2)
        if check > ans:
            ans = check
print(ans)