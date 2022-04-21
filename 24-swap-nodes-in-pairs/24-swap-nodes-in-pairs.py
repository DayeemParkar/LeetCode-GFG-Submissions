# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = None
        temp = head
        ans = ListNode()
        l = ans
        n = -1
        
        while temp:
            if n % 2 == 1:
                prev = temp
                n += 1
            else:
                ans.next = ListNode(temp.val)
                ans = ans.next
                ans.next = ListNode(prev.val)
                ans = ans.next
                n += 1
            temp = temp.next
        if n % 2 == 0:
            ans.next = ListNode(prev.val)
            ans = ans.next
        
        return l.next