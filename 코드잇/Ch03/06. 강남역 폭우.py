def trapping_rain(buildings):
    pre = buildings[0]
    water = 0
    last = 0
    max_num = max(buildings)
    for i in buildings:
        if pre == i:
            water += 0
        elif pre > i:
            if max_num ==pre:
                pre = i 
            water += pre -i
        elif pre < i:
            pre = i
    if(buildings[-1] == 1):
        water -= 1
    return water

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)