# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if len(nums) > 3:
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        elif len(nums) == 3:
            root.left, root.right = TreeNode(nums[0]), TreeNode(nums[2])
        else:
            root.left = TreeNode(nums[0])
        return root