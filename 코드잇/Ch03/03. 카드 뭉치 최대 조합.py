def max_product(left_cards, right_cards):
    max_product = 0
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다
            max_product = max(max_product, left * right)

    # 찾은 최댓값을 리턴한다            
    return max_product

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))