# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # make one pointer go ahead 1 at a time, another one 2 at a time
        incre1 = head
        incre2 = head
        while incre2.next and incre2.next.next:
            incre1 = incre1.next
            incre2 = incre2.next.next
            if incre1 == incre2:
                # if match found, keep incrementing 1st pointer and start incrementing
                # the head until both intersect, that will be cycle point
                while incre1 != head:
                    incre1 = incre1.next
                    head = head.next
                return head
        return None