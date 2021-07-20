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