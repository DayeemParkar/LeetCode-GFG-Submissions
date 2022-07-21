# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr, prev = head, None
        for _ in range(left - 1):
            prev = ptr
            ptr = ptr.next
        ogprev = prev
        for _ in range(right + 1 - left):
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        # Fixing right end
        if not ogprev:
            head.next = ptr
            head = prev
        else:
            temp = ogprev.next
            if temp:
                temp.next = ptr
            # fixing left end
            ogprev.next = prev
        return head