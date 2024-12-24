# 146


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.head = None
        self.tail = None

    def _append_to_tail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def _delete_head(self):
        temp_head = self.head.next
        self.head.next = None
        temp_head.prev = None
        del self.map[self.head.key]
        self.head = temp_head

    def _update_non_tail_node_position(self, existed_node):
        next_node = existed_node.next
        prev_node = existed_node.prev
        if existed_node is self.head:
            temp_head = existed_node.next
            existed_node.next = None
            temp_head.prev = None
            self.head = temp_head
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
            existed_node.next = None
            existed_node.prev = None
        self._append_to_tail(existed_node)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        if node is not self.tail:
            self._update_non_tail_node_position(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            new_node = Node(key=key, val=value)
            self.map[key] = new_node
            # 沒滿
            if self.size < self.capacity:
                if self.tail is None:
                    self.head = self.tail = new_node
                else:
                    self._append_to_tail(new_node)
                self.size += 1
            else:  #滿
                self._append_to_tail(new_node)
                self._delete_head()
        else:
            existed_node = self.map[key]
            existed_node.val = value
            if existed_node is not self.tail:
                self._update_non_tail_node_position(existed_node)