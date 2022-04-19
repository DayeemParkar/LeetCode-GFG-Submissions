# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if (not root) or self.found:
            return
        
        self.inorder(root.left)
        
        if self.prev:
            if self.prev.val > root.val:
                if self.n2:
                    self.found = True
                if not self.n1: 
                    self.n1 = self.prev
                self.n2 = root
        self.prev = root
        
        self.inorder(root.right)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes, self.n1, self.n2, self.prev, self.found = [], None, None, None, False
        self.inorder(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        