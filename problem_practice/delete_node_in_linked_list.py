# 237
# TC : O(1)
# SC : O(1)
"""
Since head node isn't available, value substitution is used.
"""

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
