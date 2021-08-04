col, row = input().split()
grid = [[0 for _ in range(int(row))] for _ in range(int(col))]
num = 0
for r in range(int(row)):
    if r%2 == 0:
        for c in range(int(col)):
            grid[c][r] = num
            num+=1
    else:
        for c in range(int(col)-1, -1, -1):
            grid[c][r] = num
            num+=1

for c in range(int(col)):
    for r in range(int(row)):
        print(grid[c][r], end= ' ')
    print()