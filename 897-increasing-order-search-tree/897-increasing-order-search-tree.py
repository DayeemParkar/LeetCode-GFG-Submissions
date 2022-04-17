# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: TreeNode):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        self.nodes.append(root.val)
        if root.right:
            self.inorder(root.right)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        self.inorder(root)
        newR = TreeNode(-1)
        newRCpy = newR
        
        for i in self.nodes:
            newR.right = TreeNode(i)
            newR = newR.right
        
        return newRCpy.right