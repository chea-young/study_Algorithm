def is_palindrome(word):
    count_num = len(word)//2
    for i in range(count_num):
        last_num = i*(-1) -1
        if(word[i] != word[last_num]):
            return False
    return True

# TEST
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))