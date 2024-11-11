# 160
# TC : O(m+n)
# SC : O(1)
"""
This problem is not easy ...
Use two pointer method we could eventually start at the same length away from 
the tail node.
"""


def getIntersectionNode(headA, headB):
    pointerA = headA
    pointerB = headB

    while pointerA is not pointerB:
        pointerA = headB if pointerA is None else pointerA.next
        pointerB = headA if pointerB is None else pointerB.next

    return pointerA
