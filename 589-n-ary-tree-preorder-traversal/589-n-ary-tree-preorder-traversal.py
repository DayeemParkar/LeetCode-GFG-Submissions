"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, root):
        if root:
            self.ans.append(root.val)
            for i in root.children:
                self.helper(i)
    
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.helper(root)
        return self.ans