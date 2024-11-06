from typing import Optional

# 104
# TC : O(n) traverse every node
# SC : O(1)


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_dep = self.maxDepth(root.left)
    right_dep = self.maxDepth(root.right)
    return 1 + max(left_dep,right_dep)
