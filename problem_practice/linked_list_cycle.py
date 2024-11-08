# 141
# TC : O(n)
# SC : O(1)
"""
Fast-slow algorithm.
Think of two runners running on a lap where they will end up meeting
each other.
The description is really terrible though. Why bother mentioning `pos`?
"""


def hasCycle(head) -> bool:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True
    return False


def hasCycle(head) -> bool:
    record = set()
    is_cycle = False
    curr = head
    while curr:
        if curr in record:
            is_cycle = True
            break
        record.add(curr)
        curr = curr.next
    return is_cycle
