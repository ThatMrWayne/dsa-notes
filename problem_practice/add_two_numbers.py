# 2
# TC : O(n)
# SC : O(n)


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def add_two(l1, l2):
    l1_p = l1
    l2_p = l2
    carry_out = 0
    head, prev = None, None
    while l1_p or l2_p:
        l1_val = l1_p.val if l1_p is not None else 0
        l2_val = l2_p.val if l2_p is not None else 0
        new_val = l1_val + l2_val + carry_out
        if new_val >= 10:
            carry_out = 1
            new_val = new_val%10
        else:
            carry_out = 0
        new_node = ListNode(new_val)
        if head is None:
            head = new_node
        if prev is not None:
            prev.next = new_node
        prev = new_node
        l1_p = getattr(l1_p, 'next', None)
        l2_p = getattr(l2_p, 'next', None)
    if carry_out == 1:
        new_node = ListNode(1)
        prev.next = new_node

    return head
