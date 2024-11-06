from typing import Optional

# 101
# TC : O(n)
# SC : O(n)
"""
Use BFS traverse concept to solve.
"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def check_is_symmetric(arr):
        is_symmetric = True
        i, j = 0, len(arr)-1
        while i < j:
            if getattr(arr[i], 'val', None) != getattr(arr[j], 'val', None):
                is_symmetric = False
                break
            i += 1
            j -= 1
        return is_symmetric

    parent = [root]
    child = []
    is_symmetric = True
    while parent:
        none_count = 0
        for p in parent:
            if p is None:
                continue
            if p.left:
                child.append(p.left)
            else:
                child.append(None)
                none_count += 1
            if p.right:
                child.append(p.right)
            else:
                child.append(None)
                none_count += 1
        if len(child) == none_count: # means no more child
            parent = []
        else:
            is_symmetric = check_is_symmetric(child)
            if is_symmetric:
                parent = child
                child = []
            else:
                break
    return is_symmetric
