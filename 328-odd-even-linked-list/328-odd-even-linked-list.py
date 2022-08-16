# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd = head
            even = evenHead = odd.next
            while even and even.next:
                odd.next = odd = even.next
                even.next = even = odd.next
            odd.next = evenHead
        return head