# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        
        # if any one list is empty, return other string
        if not l1:
            return l2
        if not l2:
            return l1
        
        start = ListNode(-1)
        temp = start
        
        # while none of the list are empty
        while l1 and l2:
            if l1.val <= l2.val:
                start.next = l1
                start = l1
                l1 = l1.next
            else:
                start.next = l2
                start = l2
                l2 = l2.next
        
        # if any list is not empty, empty them
        if l1:
            start.next = l1
        elif l2:
            start.next = l2
        return temp.next