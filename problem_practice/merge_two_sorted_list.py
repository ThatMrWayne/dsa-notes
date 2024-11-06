from typing import Optional

# 21
# TC : O(a)
# SC : O(1)
"""
yeah I know the code looks dumb with a bunch of if...else,
well... you know... the thinking process is what really matter.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not any((list1, list2)):
            return None
        result_head, curr_head = None, None
        while list1 and list2:
            if list1.val <= list2.val:
                if result_head is None:
                    result_head = curr_head = list1
                else:
                    curr_head.next = list1
                    curr_head = curr_head.next
                list1 = list1.next
            else:
                if result_head is None:
                    result_head = curr_head = list2
                else:
                    curr_head.next = list2
                    curr_head = curr_head.next
                list2 = list2.next
        if curr_head:
            if list1 is None:
                curr_head.next = list2
            else:
                curr_head.next = list1
        else:
            if list1:
                result_head = list1
            else:
                result_head = list2

        return result_head
