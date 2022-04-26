# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if root.val > key: root.left = self.deleteNode(root.left, key)
        elif root.val < key: root.right = self.deleteNode(root.right, key)
        else:
            if None in (root.left, root.right): return root.left or root.right
        
            n, n_parent = root.right, root
            while n.left:
                n_parent, n = n, n.left
            if n_parent is not root: n_parent.left = n.right
            else: n_parent.right = n.right
            root.val = n.val
        
        return root