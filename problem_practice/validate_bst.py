from typing import Optional

# 98
# TC : O(n) traverse every node
# SC : O(n) cuz I use `result_list`
"""
Use DFS in-order traverse to judge
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def DFS_InOrder(node, result_list):
        if node.left:
            is_valid = DFS_InOrder(node.left, result_list)
            if not is_valid:
                return False

        if len(result_list) >= 1:
            if node.val <= result_list[-1]:
                return False
        result_list.append(node.val)

        if node.right:
            is_valid = DFS_InOrder(node.right, result_list)
            if not is_valid:
                return False
        return True

    result_list = []
    is_valid = DFS_InOrder(root, result_list)
    return is_valid
