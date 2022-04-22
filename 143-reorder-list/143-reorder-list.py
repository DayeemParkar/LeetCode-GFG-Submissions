# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next: return
        
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
        
        mid, curr = p1, p1.next
        while curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = mid.next
            mid.next = temp
        
        p1, p2 = head, mid.next
        while p1 != mid:
            mid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = mid.next