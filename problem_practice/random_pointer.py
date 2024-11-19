# 138
# TC : O(n)
# SC : O(n)


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# version 1
def copyRandomList(head):
    if head is None:
        return None
    # first loop
    old_to_new = {}
    new_head, prev_new = None, None
    curr = head
    while curr:
        temp_new_node = Node(curr.val)
        if new_head is None:
            new_head = temp_new_node
        if prev_new:
            prev_new.next = temp_new_node
        old_to_new[curr] = temp_new_node
        curr = curr.next
        prev_new = temp_new_node

    # second loop
    curr = head
    while curr:
        old_random_node = curr.random
        correspond_new_node = old_to_new[curr]
        if old_random_node is None:
            correspond_new_node.random = None
        else:
            random_new_node = old_to_new[old_random_node]
            correspond_new_node.random = random_new_node
        curr = curr.next

    return new_head


# version 2
def copyRandomList(head):
    if not head:
        return None

    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    old_head = head
    new_head = head.next
    curr_old = old_head
    curr_new = new_head

    while curr_old:
        curr_old.next = curr_old.next.next
        curr_new.next = curr_new.next.next if curr_new.next else None
        curr_old = curr_old.next
        curr_new = curr_new.next

    return new_head
