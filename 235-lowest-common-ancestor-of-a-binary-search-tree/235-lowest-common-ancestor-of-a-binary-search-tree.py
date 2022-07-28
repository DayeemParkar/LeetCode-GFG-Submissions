# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        gVal, sVal = p.val, q.val
        if q.val > p.val:
            gVal, sVal = sVal, gVal
        while root:
            if root.val > gVal:
                root = root.left
            elif root.val < sVal:
                root = root.right
            else:
                return root