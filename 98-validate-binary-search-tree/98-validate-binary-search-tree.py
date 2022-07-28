# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.nodes.append(node.val)
            self.inorder(node.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.nodes = []
        self.inorder(root)
        print(self.nodes)
        for i in range(len(self.nodes) - 1):
            if self.nodes[i] >= self.nodes[i + 1]:
                return False
        return True