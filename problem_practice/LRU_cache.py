# 146


class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def _update_node_position_if_not_tail(self, existed_node):
        prev_node = existed_node.prev
        next_node = existed_node.next
        if prev_node is not None:
            prev_node.next = next_node
            next_node.prev = prev_node
            existed_node.prev = None
            existed_node.next = None
        else:
            existed_node.next = None
            next_node.prev = None
            self.head = next_node
        self.tail.next = existed_node
        existed_node.prev = self.tail
        self.tail = existed_node 


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            tar_node = self.map[key]
            if tar_node is not self.tail:
                self._update_node_position_if_not_tail(tar_node)
            return tar_node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            new_node = Node(key=key, val=value)
            self.map[key] = new_node
            # 沒滿
            if self.size < self.capacity:
                if self.tail is None:
                    self.head = self.tail = new_node
                else:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                self.size += 1
            else: #滿了
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                temp_head_next = self.head.next
                self.head.next = None
                temp_head_next.prev = None
                head_key = self.head.key
                del self.map[head_key]
                self.head = temp_head_next
        else:
            existed_node = self.map[key]
            existed_node.val = value
            if existed_node is not self.tail:
                self._update_node_position_if_not_tail(existed_node)
