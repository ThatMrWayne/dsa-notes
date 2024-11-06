from typing import List, Optional

# 108
# TC :
# SC :


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 1:
        return TreeNode(nums[0])
    if len(nums) == 0:
        return None
    else:
        head_idx = len(nums)//2
        head_node = TreeNode(nums[head_idx])
        left_head = sortedArrayToBST(nums[:head_idx])
        right_head = sortedArrayToBST(nums[head_idx+1:])
        head_node.left = left_head
        head_node.right = right_head
        return head_node
