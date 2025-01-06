#92


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        curr = head
        left_node = right_node = None
        prev_head = prev_tail = None
        n = 1
        prev = None
        while curr:
            if n == left:
                left_node = curr
                prev_head = prev
            if n == right:
                right_node = curr
                break
            prev = curr
            curr = curr.next
            n += 1
        if left_node is right_node:
            return head
        else:
            prev_tail = right_node.next
            right_node.next = None

            first = left_node
            second = first.next
            first.next = None
            while second:
                temp = second.next
                second.next = first
                first, second = second, temp
            # first is new head
            if prev_head is not None:
                prev_head.next = first
            left_node.next = prev_tail
            if prev_head is None:
                return first
            else:
                return head
