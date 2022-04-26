# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        A, P = [], []
        def dfs(N):
            if N == None: return
            P.append(N.val)
            if (N.left, N.right) == (None, None) and sum(P) == targetSum: A.append(list(P))
            else: dfs(N.left), dfs(N.right)
            P.pop()
        dfs(root)
        return A