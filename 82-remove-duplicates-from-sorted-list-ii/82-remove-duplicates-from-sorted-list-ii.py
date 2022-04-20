# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ans = ListNode(-1, head)
        p1, p2 = ans, head
        while p2:
            while p2.next and p2.val==p2.next.val:
                p2 = p2.next 
            if p1.next == p2:
                p1 = p1.next
                p2 = p2.next
            else:
                p2 = p2.next
                p1.next = p2
        return ans.next