"""
NOTE
 - 1초마다 시계방향으로 돌아간다.
"""
num, sec = input().split()

def rotate(c_list):
    down = c_list[0][-1:]
    up = c_list[1][-1:]
    c_list[0] = up + c_list[0][:-1]
    c_list[1] = down+ c_list[1][:-1]
    return c_list

c_list = []
for element in range(2):
    e_list = input().split()
    c_list.append(e_list)

for r in range(int(sec)):
    c_list = rotate(c_list)

for element in c_list:
    for j in element:
        print(j, end=" ")
    print()