# 3
# TC : O(n)
# SC : O(1) since constraints say s consists of English letters, digits, symbols and spaces
"""
This one almost burn my head ...
"""



# first version
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    idx_record = {s[-1]: len(s)-1}
    low, high = len(s)-1, len(s)
    curr_set = {s[-1]}
    curr_length = max_length = 1
    for i in range(len(s)-2, -1, -1):
        if s[i] in curr_set:
            low = i
            high = idx_record[s[i]]
            idx_record[s[i]] = i
            curr_set = set(s[low:high])
            curr_length = high - low
        else:
            idx_record[s[i]] = i
            curr_length += 1
            curr_set.add(s[i])

        max_length = curr_length if curr_length > max_length else max_length

    return max_length


# second version
def lengthOfLongestSubstring2(s):
    if len(s) == 0:
        return 0
    low = high = len(s)-1
    curr_set = {s[-1]}
    curr_length = max_length = 1
    for low in range(len(s)-2, -1, -1):
        while s[low] in curr_set:
            curr_set.remove(s[high])
            high -= 1

        curr_set.add(s[low])
        curr_length = high - low + 1
        max_length = max(curr_length, max_length)

    return max_length
