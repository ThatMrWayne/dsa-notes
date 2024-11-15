# 5
# TC : O(n^2)
# SC : O(1)


def longestPalindrome(s: str) -> str:
    def gen_palindrome(left_idx, right_idx):
        while left_idx >=0 and right_idx < len(s):
            if s[left_idx] == s[right_idx]:
                left_idx -= 1
                right_idx += 1
            else:
                break
        return left_idx, right_idx

    max_len = 0
    start, end = None, None
    for i in range(len(s)):
        temp_max_len = 0
        left_idx, right_idx = None, None
        # case 1
        left_idx_1 = i-1
        right_idx_1 = i+1
        left_idx_1, right_idx_1 = gen_palindrome(left_idx_1, right_idx_1)
        temp_max_len = right_idx_1 - left_idx_1 - 1
        left_idx, right_idx = left_idx_1, right_idx_1
        # case 2
        left_idx_2, right_idx_2 = i-1, i+1
        if i+1 < len(s) and s[i] == s[i+1]:
            left_idx_2, right_idx_2 = gen_palindrome(i-1, i+2)

        if (right_idx_2 - left_idx_2 - 1) > temp_max_len:
            left_idx, right_idx = left_idx_2, right_idx_2
            temp_max_len = right_idx_2 - left_idx_2 - 1

        if temp_max_len > max_len:
            start, end = left_idx, right_idx
            max_len = end - start - 1

    return s[start+1:end]
