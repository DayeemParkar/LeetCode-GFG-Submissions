class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.helper(list(range(1, 10)), k, n, [])
        
        return self.ans
    
    def helper(self, nums, k, n, currPath):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            self.ans.append(currPath)
        for i in range(len(nums)):
            self.helper(nums[i + 1:], k - 1, n - nums[i], currPath + [nums[i]])