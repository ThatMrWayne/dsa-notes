from typing import Optional

# 206
# TC : O(n)
# SC : O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    first = head
    second = first.next
    head.next = None
    while second:
        temp = second.next
        second.next = first
        first, second = second, temp
    head = first
    return head
