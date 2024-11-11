# 234
# TC : O(n)
# SC : O(1)
"""
1. Find mid point and reverse the rest half linked list.
2. Iterate from both starting node to check.
Note:
Use fast-slow algorithm to find the mid point.
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def isPalindrome(head) -> bool:
    def reverse(head):
        first = head
        second = head.next
        head.next = None
        while second:
            temp = second.next
            second.next = first
            first, second = second, temp
        head = first
        return head

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid_point = slow

    right_head = reverse(mid_point)
    left_head = head
    is_valid = True
    while True:
        if left_head.val != right_head.val:
            is_valid = False
            break
        if left_head is mid_point or right_head is mid_point:
            break
        left_head = left_head.next
        right_head = right_head.next
    return is_valid
