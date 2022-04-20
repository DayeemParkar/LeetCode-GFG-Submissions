# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA, nodeB, lA, lB = headA, headB, 0, 0
        while nodeA and nodeB:
            nodeA, nodeB, lA, lB = nodeA.next, nodeB.next, lA + 1, lB + 1
        while nodeA:
            nodeA, lA = nodeA.next, lA + 1
        while nodeB:
            nodeB, lB = nodeB.next, lB + 1
        
        nodeA, nodeB = headA, headB
        while lA > lB:
            nodeA, lA = nodeA.next, lA - 1
        while lB > lA:
            nodeB, lB = nodeB.next, lB - 1
        while nodeA != nodeB:
            nodeA, nodeB = nodeA.next, nodeB.next
        return nodeA