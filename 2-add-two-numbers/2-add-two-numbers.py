# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        c = 0
        num2 = 0
        
        # first go through both listnodes to get the numbers
        while l1 != None and l2 != None:
            num1 = l1.val * pow(10, c) + num1
            num2 = l2.val * pow(10, c) + num2
            c += 1
            l1 = l1.next
            l2 = l2.next
        
        # case where both listnodes might have different length
        while l1 != None:
            num1 = l1.val * pow(10, c) + num1
            c += 1
            l1 = l1.next
        while l2 != None:
            num2 = l2.val * pow(10, c) + num2
            c += 1
            l2 = l2.next
        
        #find and store the sum
        s = num1 + num2
        temp = ListNode(s % 10, None) # initialize linked list
        result = temp
        s //= 10
        while s > 0:
            temp.next = ListNode(s % 10, None)
            temp = temp.next
            s //= 10
        
        return result
        