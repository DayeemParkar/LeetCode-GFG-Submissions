# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseHelper(self, head, k, leftNodes):
        if leftNodes < k:
            return head
        count = 0
        prev = None
        current = head
        while current and count < k:
            count += 1
            leftNodes -= 1
            next = current.next
            current.next = prev
            prev = current
            current = next
        if next:
            head.next = self.reverseHelper(next, k, leftNodes)
        return prev
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        leftNodes, node = 0, head
        while node:
            leftNodes += 1
            node = node.next

        return self.reverseHelper(head, k, leftNodes)