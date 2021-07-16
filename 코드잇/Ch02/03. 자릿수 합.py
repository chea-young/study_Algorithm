# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    digit_string = str(n)
    if len(digit_string) == 1:
        return int(digit_string)
    else:
        return sum_digits(digit_string[:-1]) + sum_digits(digit_string[-1])

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))